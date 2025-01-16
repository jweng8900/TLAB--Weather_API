import pandas as pd

# Create a jupyter notebook in the folder titled `notebooks` called `data_transform.py`. Within this file you will be create the following dataframes and save them as a csv files into your folder `data/csv`.

# * monthly medians on `temperature`, `relative humidity`, `precipitation`, and `surface pressure` for all available months
# * yearly medians on `temperature`, `relative humidity`, `precipitation`, and `surface pressure` for all available years
# * yearly medians on `temperature`, `relative humidity`, `precipitation`, and `surface pressure` for all available years along with harvest data (`million_60kgs_bag`, `nonbear_mill_trees`, `bear_mill_trees`, `avg_unemp_perc`) for each respective year present for Minas Gerais

# Be sure to drop rows that contain missing values as you perform these data transformations.

df=pd.read_csv('data/csv/weather_data.csv')

print(df.head())