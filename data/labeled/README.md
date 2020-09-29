# Pre-Labeled Datasets
This document provides example phenomena which have labeled datasets. You may choose to use any of the provided phenomena for your detection model.

## Transverse Cirrus Bands (TCB) 

TCBs are bands of clouds oriented perpendicular to the atmospheric flow in which they are embedded. TCBs are often an indicator of strong turbulence and often associated with severe weather such as hurricanes and thunderstorms or atmospheric jets.
* Image Labeler Transverse Cirrus Bands Data: s3://impact-datashare/transverse_bands/


## Cloud Streets

Cloud streets are extended lines of cumulus clouds oriented parallel to the atmospheric flow. Cloud streets are known to be significant to the vertical transport of heat, moisture, air pollutants, and momentum within the atmosphere. 
* Image Labeler Cloud Streets Data: s3://impact-datashare/cloudstreet


## High Latitude Dust

High Latitude Dust (HLD) consists of a mixture of solid and liquid particles suspended in the atmosphere varying in composition, source and size. Dust storms and transport can have extensive climate and societal impacts.
* HLD Data: s3://impact-datashare/hld-labeled


## Biomass Burning Smoke

Smoke is the mixture of gas and particulates in the atmosphere resulting from the combustion of biomass. Smoke from events such as wildfires and agricultural burning may be transported thousands of kilometers and causes numerous health impacts. The training and validation folders can be found using the link provided. The files are in the .tif and .bmp formats.
* Smoke Data: s3://impact-datashare/smoke-labeled

## Air Quality Data

Monitoring surface air quality helps ensure the protection of human health and property. However, surface air quality data is sparsely monitored. To help fill in these gaps, inferences are derived from other sources including remote sensing. The CSV formatted data and labels are provided below. It contains the following fields which have been described.

1. station_id: Unique identifier of the PM 2.5 monitors stationed across US
2. stime: Time and date of sample recorded
3. air_data_value: EPA air data PM2.5 readings
4. RH: relative humidity from HRRR
5. UGRD, VGRD: Wind speed vectors from HRRR
6. HPBL: Height of Planetary Boundary Layer from HRRR
7. TMP: Temperature recorded from HRRR
8. goes_measurement: AOD reading from GOES R

* Air Quality Data: s3://impact-datashare/pm2.5-labeled

# How to download data from aws s3 buckets

1. Download and install AWS Command Line Interface (CLI). More information can be found [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
2. use `aws s3 cp <s3://link/to/folder/>  <path/to/save> --recursive --no-sign-request`
