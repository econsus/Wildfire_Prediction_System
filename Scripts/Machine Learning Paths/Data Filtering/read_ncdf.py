import netCDF4 as nc
import numpy as np
import os

#Specify file path and name
folder_path = 'F:\Kuliah\Bangkit\Capstone Project\Project\ERA-5 Data'
file_name = 'Surface latent heat flux.nc'
file_path = folder_path + '\\' + file_name

#Open the nt file
data = nc.Dataset(file_path, 'r' )
print(data)

#print the variables name
# print(data.variables.keys())

#check each variables
time = data.variables['time']
lon = data.variables['longitude']
lat = data.variables['latitude']
slhf = data.variables['slhf']
# print(time)
# print(lon)
# print(lat)
print(slhf)

#Accesing the data from variables
time_data = data.variables['time'][:]
lon_data = data.variables['longitude'][:]
lat_data = data.variables['latitude'][:]
slhf_data = data.variables['slhf'][:]
# print(time_data)
# print(lon_data)
# print(lat_data)
print(slhf_data)