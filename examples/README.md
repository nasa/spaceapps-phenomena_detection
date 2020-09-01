# Code Examples
## Download Script Readme

To run the shapefile download script present in the folder this readme provides the steps to do so.
Requirements:
* Python and pip (`pip install -r requirements.txt`)
* Data from the [ImageLabeler](https://labeler.nasa-impact.net/earth-science-events/list)
* Select any existing phenomena or a new phenomena (ask admins to create one for you)
    * While drawing bounding boxes, if Aqua and TrueColor are not used, make sure to change the URL by using the image_url function
* Click on download all, extract the zip to a place that contains the script as well

Running the code:
* Run the code from the ipython file
* Or alternatively copy the code in a python file and change directory to the labeled folder and run `python file_name.py`
* Successful execution of the code will result in an Output directory and tif and bmp files for each shapefile in the input folder

The final folder structure will look similar to the following:<br>
image_labeler_shapefile_downloader/<br>
--- README.md<br>
--- image_labeler_data_download.ipynb<br>
--- downloaded_layer/<br>
------ {phenomena}_{date}_{user}_{id}/<br>
---------- {phenomena}_{date}_{user}_{id}.shp<br>
---------- {phenomena}_{date}_{user}_{id}.dbf<br>
---------- {phenomena}_{date}_{user}_{id}.prj<br>
---------- {phenomena}_{date}_{user}_{id}.shx<br>
------ {phenomena}_{date}_{user}_{id_1}/<br>
---------- {phenomena}_{date}_{user}_{id_1}.shp  <br>
---------- {phenomena}_{date}_{user}_{id_1}.dbf  <br>
---------- {phenomena}_{date}_{user}_{id_1}.prj<br>
---------- {phenomena}_{date}_{user}_{id_1}.shx<br>
--- Output/<br>
------ {phenomena}_{datetime}_{bounding_box}.tif<br>
------ {phenomena}_{datetime}_{bounding_box}.bmp<br>


## Detection Model Readme

The shapefile download script provided above iterates through shapefiles downloaded from image-labeler. The shapefiles are converted into pairs of input and label images and stored in ML ready format.

The example notebook below is a model using neural networks for dust detection. The script trains a model on High Latitude Dust (HLD) images and performs new detections for the model validation. The model metrics such as accuracy, precision, and recall are calculated and can be improved by tuning the hyperparameters. 

The final output contains an instance of visualization of the dust detections on the original images. Please use this example to help create your own phenomena detection model and be as creative as possible for visualizing detections. 
