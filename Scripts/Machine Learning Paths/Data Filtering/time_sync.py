import numpy as np
from time_conversion import convert_time
import pandas as pd

def time_sync(input_file, output_file):
    # Read the CSV file using pandas
    csv_data = pd.read_csv(input_file)

    converted_times = []
    row_num = 0
    # Set print options to suppress scientific notation
    for index, row in csv_data.iterrows():
        year = row[0]
        month = row[1]
        day = row[2]
        time = row[3]
        converted_times.append(convert_time(year, month, day, time))
        print(row_num)
        row_num = row_num + 1

    # Create a DataFrame with Converted_Time as the first column
    result_df = pd.DataFrame({'Time': converted_times})

    # Concatenate the DataFrame with the remaining columns from csv_data (5th, 6th, and 7th columns)
    result_df = pd.concat([result_df, csv_data.iloc[:, 4:7]], axis=1)

    # Save the DataFrame to a new CSV file with headers
    result_df.to_csv(output_file, index=False, header=['Time', 'lat', 'lon', 'Heat_Level'])

# Example Usage
example_file_path = 'Scripts/Machine Learning Paths/Data Filtering/output/stripped_data.csv'
output_file_path = 'Scripts/Machine Learning Paths/Data Filtering/output/converted_times.csv'
time_sync(example_file_path, output_file_path)
