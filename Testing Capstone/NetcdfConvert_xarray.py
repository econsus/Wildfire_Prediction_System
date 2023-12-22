import pandas as pd
import xarray as xr

def convert(file):
  df= xr.open_dataset(file)
  df=df.to_dataframe()
  return df