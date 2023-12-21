import os
import netCDF4 as nc
import numpy as np

def extract_coordinate(file_path):
    data = nc.Dataset(file_path, 'r')
    lat_data = data.variables['latitude'][:]
    lon_data = data.variables['longitude'][:]

    # for lat_value in lat_data:
    #     lat_array = np.append(lat_array, lat_value)
    # for lon_value in lon_data:
    #     lon_array = np.append(lon_array, lon_value)

    # lon_array = np.transpose(lon_array)
    # lat_array = np.transpose(lat_array)

    lat_array = np.round(np.array(lat_data), 2)
    lon_array = np.round(np.array(lon_data), 2)

    # print(lat_array, lon_array)

    np.savetxt('lat_array.csv', lat_array, fmt='%.2f', delimiter=',')
    np.savetxt('lon_array.csv', lon_array, fmt='%.2f', delimiter=',')

if __name__ == '__main__':
    folder_path = 'F:\\Kuliah\\Bangkit\\Capstone Project\\Project\\ERA-5 Data'
    file_name = 'Surface latent heat flux.nc'
    file_path = os.path.join(folder_path, file_name)

    extract_coordinate(file_path)