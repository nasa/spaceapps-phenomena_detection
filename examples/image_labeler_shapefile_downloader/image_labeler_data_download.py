"""
Functions to handle feature shapes
"""
import fiona
import requests
import os
import re
from datetime import datetime
import rasterio.features
import numpy as np

from io import BytesIO
from PIL import Image


# use this if you are using anything else than Aqua and TrueColor to generate the image in the image labeler
def image_url(query_date, bbox, sensor, product, width, height):
    BASE_URL = 'https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi'
    param_dict = {
        "BBOX": bbox,
        "CRS": "EPSG:4326",
        "FORMAT": "image/jpeg",
        "HEIGHT": height,
        "LAYERS": "MODIS_%s_CorrectedReflectance_%s" % (sensor, product),
        "REQUEST": "GetMap",
        "SERVICE": "WMS",
        "TIME": query_date,
        "TRANSPARENT": "false",
        "VERSION": "1.3.0",
        "WIDTH": width,
    }

    return "{}?{}".format(BASE_URL, urlencode(param_dict))

# NOTE: Use image_url function above to create a valid url, if the shapefile generation was not done in Aqua, TrueColor 
URL = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap&layers=MODIS_Aqua_CorrectedReflectance_TrueColor&version=1.3.0&crs=EPSG:4326&transparent=false&width={}&height={}&bbox={}&format=image/tiff&time={}"
KM_PER_DEG_AT_EQ = 111.

def calculate_width_height(extent, resolution):
    """
    extent: [lower_latitude, left_longitude, higher_latitude, right_longitude], EG: [51.46162974683544,-22.94768591772153,53.03698575949367,-20.952234968354432]
    resolution: represents the pixel resolution, i.e. km/pixel. Should be a value from this list: [0.03, 0.06, 0.125, 0.25, 0.5, 1, 5, 10]
    """
    lats = extent[::2]
    lons = extent[1::2]
    km_per_deg_at_lat = KM_PER_DEG_AT_EQ * np.cos(np.pi * np.mean(lats) / 180.)
    width = int((lons[1] - lons[0]) * km_per_deg_at_lat / resolution)
    height = int((lats[1] - lats[0]) * KM_PER_DEG_AT_EQ / resolution)
    return (width, height)


def modis_url(time, extent, resolution):
    """
    time: utc time in iso format EG: 2020-02-19T00:00:00Z
    extent: [lower_latitude, left_longitude, higher_latitude, right_longitude], EG: [51.46162974683544,-22.94768591772153,53.03698575949367,-20.952234968354432]
    resolution: represents the pixel resolution, i.e. km/pixel. Should be a value from this list: [0.03, 0.06, 0.125, 0.25, 0.5, 1, 5, 10]
    """
    width, height = calculate_width_height(extent, resolution)
    extent = ','.join(map(lambda x: str(x), extent))
    return (width, height, URL.format(width, height, extent, time))


def explode(coords):
    """Explode a GeoJSON geometry's coordinates object and yield coordinate tuples.
    As long as the input is conforming, the type of the geometry doesn't matter."""
    for e in coords:
        if isinstance(e, (float, int)):
            yield coords
            break
        else:
            for f in explode(e):
                yield f


def get_bbox(fiona_shape, offset=0):
    x, y = zip(*list(explode(fiona_shape['geometry']['coordinates'])))
    return min(y) - offset, min(x) - offset, max(y) + offset, max(x) + offset


def bitmap_from_shp(fiona_shape, transform, img_shape):
    """ extract out the smoke pixels using the shapefile
     from the transform defined
    Args:
        fiona_shape (Collection): fiona shape collection obtained by fiona.open()
        transfrom (rasterio.transfrom.Affine): rasterio transform object
    """
    geoms = []
    y_mtx = np.zeros((img_shape))
    for shape in fiona_shape:
        geoms.append(shape["geometry"])

    # raster the geoms onto a bitmap
    geom_map = [(geo, 255) for geo in geoms]
    y_mtx = rasterio.features.rasterize(
        geom_map,
        out_shape=(img_shape[0], img_shape[1]),
        transform=transform
    )

    return y_mtx


input_folder = "downloaded_layers"
for folder in os.listdir(input_folder):
    internal_folder = f'{input_folder}/{folder}'
    if not os.path.isdir(internal_folder):
        continue

    val = f"{internal_folder}/{folder}.shp"
    with fiona.open(val) as shapefile:
        bounding_box = get_bbox(shapefile[0])
        phenomena = folder.split("_")[0]

        date = re.findall(r"\d{4}-\d{2}-\d{2}", folder)[0]

        width, height, url = modis_url(
            f'{date}T00:00:00Z',
            bounding_box,
            0.25
        )

        date = datetime.strptime(date, "%Y-%m-%d")
        day_of_year = str(date.timetuple().tm_yday).zfill(3)
        datetimestr = f'{date.year}{day_of_year}000000'

        # get the tiff
        response = requests.get(url)
        img = BytesIO(response.content)

        # get the bitmap
        btm = None
        with rasterio.open(img) as dataset:
            btm = bitmap_from_shp(shapefile, dataset.transform, (height, width))

        bbox_str = ",".join([str(bb) for bb in bounding_box])
        name = f'phenomena-{phenomena}-datetime-{datetimestr}-bbox-{bbox_str}'
        with open(f"output/{name}.tif", "wb") as write_file:
            write_file.write(img.getbuffer())

        image = Image.fromarray(btm)
        image.save(f'output/{name}.bmp')
