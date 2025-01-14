import requests
import json
import os
import pandas as pd


# Define the API URL
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"
# Make the GET request to fetch the data
page = requests.get(URL)


print(page.status_code)

data=page.json()


data_folder= 'weather_api/data/json'
file_path=os.path.join(data_folder,"weather_data.json")

with open(file_path, 'w') as file:
    data=json.dump(data, file, indent=4)

