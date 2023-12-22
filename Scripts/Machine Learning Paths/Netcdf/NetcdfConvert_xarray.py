import pandas as pd
import xarray as xr

df= xr.open_dataset('lvc.nc')

df.to_dataframe().to_csv('lvc_csv.csv')