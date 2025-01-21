# TLAB--Weather_API

The goal of this lab is to analyze weather trends in Brazil and predict the output of non-durable consumer goods at harvest time.

The relative humidity, precipitation, temperature, surface pressure, soil temperature, and soil moisture in Minas Gerais(lat: -21.72,  long: -45.39) from Jan 1 2022 to Dec 31 2023 data was collected using the open-meteoLinks to an external site. weather API.

weather_api.py shows the process of requesting data from weather API website and converting the data from JSON to csv file saved in csv folder. In the process we needed to create a data frame to convert to csv file.

data_transform jupyter notebook shows the process of transforming the weather data into monthly and yearly csv file after filtering out variable we are not interested and checking for nulls. We needed to convert time into date time frame to correctly merge the brazil csv data files together with weather csv. During this processes we used resampling and simple pandas method and functions. 

explore_weather jupyter notebook shows the analysis part of the lab where we created plots to dispaly weather and brazil csv data. We were able to draw some insights about Minas Gerias coffee exports with weather data. 