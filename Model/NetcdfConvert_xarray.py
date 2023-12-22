import pandas as pd
import xarray as xr

df= xr.open_dataset('sshf_2023.nc')

df.to_dataframe().to_csv('sshf_2023.csv')