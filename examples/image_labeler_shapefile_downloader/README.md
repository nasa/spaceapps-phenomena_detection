To run the script present in the folder this readme is at

Requirements:
1) Python and pip (`pip install -r requirements.txt`)
2) Data from the [ImageLabeler](https://labeler.nasa-impact.net/earth-science-events/list)
    2.1) Select any existing phenomena or a new phenomena (ask admins to create one for you)
        2.2.1) While drawing bounding boxes, if Aqua and TrueColor are not used, make sure to change the URL by using the iamge_url function
    2.2) Change the download type of the first entry to geojson from shapefiles
    2.3) Click on download all, extract the zip to a place that contains the script as well

RUNNING THE CODE
* Run the code from the ipython file
* Or alternatively run the python file. To do so, change directory to the examples/image_labeler_shapefile_downloader folder and run `python file_name.py`
* Successfull execution of the code will result in an 'output' directory and tif and bmp files for each shapefile in the input folder


The folder structure will look something like this
image_labeler_shapefile_downloader (folder)
|-> README.md
|-> image_labeler_data_download.ipynb
|-> downloaded_layer(folder)
|  --> {phenomena}_{date}_{user}_{id} (folder)
|    --> {phenomena}_{date}_{user}_{id}.shp
|    --> {phenomena}_{date}_{user}_{id}.dbf
|    --> {phenomena}_{date}_{user}_{id}.prj
|    --> {phenomena}_{date}_{user}_{id}.shx
|  --> {phenomena}_{date}_{user}_{id_1} (folder)
|    --> {phenomena}_{date}_{user}_{id_1}.shp  
|    --> {phenomena}_{date}_{user}_{id_1}.dbf  
|    --> {phenomena}_{date}_{user}_{id_1}.prj
|    --> {phenomena}_{date}_{user}_{id_1}.shx
|-> Output(folder)
|  --> {phenomena}_{datetime}_{bounding_box}.tif
|  --> {phenomena}_{datetime}_{bounding_box}.bmp


The code only provides a framework of what can be done. Users are encouraged to change whatever needs to be changed in order to get the desired output