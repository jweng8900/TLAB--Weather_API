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
hourly_data = data["hourly"]

# Create a DataFrame from the dictionary
df = pd.DataFrame(hourly_data)

# Define the folder path to save the CSV data
data_folder_csv = 'data/csv'
os.makedirs(data_folder_csv, exist_ok=True)  # Ensure the folder exists
csv_path = os.path.join(data_folder_csv, 'weather_data.csv')

# Save the DataFrame to a CSV file in the 'data/csv' folder
df.to_csv(csv_path, index=False)
