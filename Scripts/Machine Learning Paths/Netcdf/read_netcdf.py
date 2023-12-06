import netCDF4 as nc

def read_netcdf(file_path):
    # Open the NetCDF file
    with nc.Dataset(file_path, 'r') as nc_file:
        # Print global attributes
        print("Global attributes:")
        for attr_name in nc_file.ncattrs():
            print(f"{attr_name}: {getattr(nc_file, attr_name)}")

        # Print information about each variable
        print("\nVariables:")
        for var_name, var in nc_file.variables.items():
            print(f"\nVariable: {var_name}")
            print(f"Dimensions: {var.dimensions}")
            print(f"Shape: {var.shape}")
            print(f"Attributes:")
            for attr_name in var.ncattrs():
                print(f"  {attr_name}: {getattr(var, attr_name)}")

            # If you want to read and print the variable values, uncomment the following lines:
            variable_values = var[:]
            print(f"Values: {variable_values}")

if __name__ == "__main__":
    # Specify the path to your NetCDF file
    file_path = "Data\ERA-5 Data\Low vegetation cover.nc"
    
    # Call the function to read and print information about the NetCDF file
    read_netcdf(file_path)
