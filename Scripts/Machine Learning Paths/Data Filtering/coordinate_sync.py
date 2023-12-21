import os
import numpy as np
import pandas as pd

def coordinate_sync(target_file, lat_file, lon_file):
    target = pd.read_csv(target_file)

    lat_array = pd.read_csv(lat_file).values.flatten()
    lon_array = pd.read_csv(lon_file).values.flatten()

    # Round the lat and lon values in the target DataFrame
    target['lat'] = target['lat'].apply(lambda x: min(lat_array, key=lambda y: abs(y - x)))
    target['lon'] = target['lon'].apply(lambda x: min(lon_array, key=lambda y: abs(y - x)))

    print(target)
    return target

if __name__ == "__main__":
    file_folder = 'Scripts\\Machine Learning Paths\\Data Filtering'
    target_file = 'output\\converted_times.csv'
    lat_file = 'Scripts\\Machine Learning Paths\\Data Filtering\\coordinate array\\lat_array.csv'
    lon_file = 'Scripts\\Machine Learning Paths\\Data Filtering\\coordinate array\\lon_array.csv'
    
    result = coordinate_sync(os.path.join(file_folder, target_file), lat_file, lon_file)

    # Save the result to a new CSV file
    result.to_csv(os.path.join(file_folder, 'output\\rounded_coordinates.csv'), index=False)
