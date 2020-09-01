If you decide to use raw data, you will need to first choose and download your data, and then you will need to label it. In this readme we have provided links to data sources as well as instructions for using the tool ImageLabeler for labeling your data.

# Data Sources
## NASA CMR

NASA's Common Metadata Repository (CMR) is a metadata system that catalogs all data and service metadata records for NASA's Earth Observing System Data and Information System (EOSDIS). You can obtain any NASA owned, publicly available dataset through CMR or its API.

* [NASA CMR Website](https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/cmr)
* [CMR API Endpoint](https://cmr.earthdata.nasa.gov/search)
* [NASA CMR API Documentation](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html)
* [Example Notebook](cmr_search_example.ipynb)

## Earthdata Search

Earthdata Search is the user-friendly frontend to CMR. Using this service, you can find satellite datasets and filter them by parameters such as science keywords, dates, platforms and instruments, data format, and location. 

* [Earthdata Search](https://search.earthdata.nasa.gov/search)
* [Getting Started Guide](https://earthdata.nasa.gov/learn/getting-started)


## GIBS Worldview

Global Imagery Browse Services (GIBS) provides over 900 datasets of globally available NASA satellite imagery in full resolution. The satellite imagery can be rendered in your own web client or GIS application. Users can also get location and time information of some Earth science events such as wildfires, volcanoes, and algal blooms. The links below provide the extended description and a sample script to download GIBS imagery.

* [Worldview Data Viewer](https://worldview.earthdata.nasa.gov/)
* [GIBS Satellite Image Search](https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs)
* [MODIS Image Downloader](https://github.com/NASA-IMPACT/data_share/blob/master/examples/url_generator.ipynb)

## GOES Satellite Data

GOES satellites 16 and 17 provide atmospheric and Earth surface imagery across the Western Hemisphere every 10 minutes. Because they stay above a fixed spot on the surface, they are able to provide consistent data of the same location over time. 

These files are stored in compressed NETCDF formats and can be accessed through [AWS S3 buckets](https://registry.opendata.aws/noaa-goes/). The raw files need to be processed for obtaining RGB images. 

* [GOES 16/17 data on AWS](https://registry.opendata.aws/noaa-goes/)
* [GOES Documentation](https://docs.opendata.aws/noaa-goes16/cics-readme.html)


# Image Labeler Documentation and Website

The Image Labeler is an interactive application created by the development team at NASA IMPACT designed to help users generate tagged images for machine learning. Images can be uploaded directly, or users can extract images from an interactive satellite map. Labeled images can also be downloaded for training your detection model.

[Image Labeler Tool](https://labeler.nasa-impact.net)
[Image Labeler Documentation](https://nasa-impact.github.io/image_labeler_docs/html/index.html#)

## Image Labeler's Data

All image data for a given event inside the Image Labeler application falls into two main 
classifications; *labeled* and *unlabeled*. *Unlabeled* data has been organized into an Earth 
Science Event category and any particular image may or may not actually show the event. This data is also referred to as *untagged*.

*Labeled* (or *tagged*) data has been manually reviewed and further refined with a status of 
*present* or *not present*, indicating whether the phenomenon in question is shown or not in the given image. This data is ready to be downloaded and used for analysis and training.

For this challenge, *labeled* data is available for immediate download (see below for directions). Alternatively, there is an option to upload, select, and tag your own images to create a custom dataset. 


## Labeling Images

To begin labeling, you will first need to upload your own set of images. Documentation on this topic can be [found here.](https://nasa-impact.github.io/image_labeler_docs/html/sectionfour.html) The linked 
page explains how to populate an event by either uploading images or extracting them from satellite data.

Once you're satisfied with the *unlabeled* images contained inside an event, you can start assigning labels. A walkthrough of how to classify images as *present* or *not present* is 
[shown here.](https://nasa-impact.github.io/image_labeler_docs/html/sectionfive.html)


## Downloading Labeled Images

Now that you have chosen a set of *labeled* images, it is time to download this data from Image Labeler. 
There are a couple ways to download images depending on what exactly you are looking for.

When browsing the Earth Science Events list page, two download options are given. First is the  **Bulk Download** button in the top right. Clicking this button will give the option to download all images(both *labeled* and *unlabeled*) for any selected events. The use of *Shift+Click* or  *Ctrl+Click* allows multiple events to be downloaded at once. 

A download button is also given for each event in the list. When clicked, a pop-up menu will prompt for which combination of *unlabeled*, *present*, or *not present* images you wish to download.

Lastly, when inside an event page, individual images can be selected and downloaded. This is useful for downloading a subset of images already classified into one of the aforementioned categories. 
Directions for performing this download can be [found here.](https://nasa-impact.github.io/image_labeler_docs/html/sectionsix.html#images)
