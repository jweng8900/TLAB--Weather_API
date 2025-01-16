import requests
import json
import os
import pandas as pd

# Define the API URL
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

# Make the GET request to fetch the data
page = requests.get(URL)

# Print the status code to ensure the request was successful
print(page.status_code)

# Load the response data into a JSON object
data = page.json()

# Define the folder path to save the JSON data
data_folder = 'data/json'
os.makedirs(data_folder, exist_ok=True)  # Ensure the folder exists
file_path = os.path.join(data_folder, "weather_data.json")

# Save the fetched data into a JSON file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

# Extract the 'hourly' data from the fetched data
hourly_data = data.get('hourly', {})

# Prepare the data to be saved into a DataFrame
json_data = {
    "time": hourly_data.get("time", []),
    "temperature_2m": hourly_data.get("temperature_2m", []),
    "relative_humidity_2m": hourly_data.get("relative_humidity_2m", []),
    "precipitation": hourly_data.get("precipitation", []),
    "surface_pressure": hourly_data.get("surface_pressure", [])
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(json_data)

# Save the DataFrame to a CSV file
df.to_csv('weather_data.csv', index=False)

data_folder = 'data/csv'
os.makedirs(data_folder, exist_ok=True)  # Ensure the folder exists
file_path = os.path.join(data_folder, "weather_data.csv")

# Save the fetched data into a JSON file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("CSV file has been created: 'weather_data.csv'")
