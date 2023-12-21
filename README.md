# Wildfire Prediction System
This is a repository consisting of project used for Bangkit 2023 Batch 2 Capstone Project

# Tools/resource we used
Google Cloud Run
Data from Era-5 Satellite used for parameter for ML model training, taken from Copernicus Climate Data Store
Data from Himawari-8 Satellite used for labelling for ML model training.

# Setting up server in Google Cloud Run
Deploy use Cloud Run Steps:
1. Install all modules that needed like Flask, numpy, pandas, tensorflow, gunicorn, Werkzeug.
2. Write main.py (Flask App, Tensorflow) based on ML model. Flask needed to route also Load the .keras/.h5 file into Website. here's the explanation:
	Flask App include: - importing os, numpy, pandas, tensorflow, and Flask.
	Function: Load .keras model, normalization, app.route, predict (input data as JSON), data reshape and 	normalize, prediction using the model, return the prediction with jsonify.
	App run in 0.0.0.0 PORT 8080.
3. Create test.py (later will be placed in .dockerignore) and test main.py on localhost.
4. Create a new project or use an existing one but specialize in capstone projects.
5. Activate: Cloud Run API and Cloud Build API
6. Install and init Google Cloud SDK by followed link:
	https://cloud.google.com/sdk/docs/install
7. Write Dockerfile (to Containerize), requirements.txt (Module that we used), .dockerignore (Any file that we don't need to push/deploy into Cloud Run.
8. Cloud build and Deploy by execute this Command in Cloud SDK
	cd (file path)
	gcloud build submit --tag gcr.io/<project_id>/<function>
	gcloud run deploy --image gcr.io/<project_id>/<function> --platform managed
		name the service for example: getpredict
		choose the location for example: 9.asia-southeast2(Jakarta)
		Allow unauthenticated invocations
		Deploy Y/N, Y
		wait, and done.

# Transforming ERA-5 data and used it on making model
To create the models:

1. Convert every raw NetCDF data into csv format by running the 'NetcdfConvert_xarray.py' file with the NetCDF file
2. Then sorting the converted NetCDF data by running the 'Sorting NetCDF CSV.py' so it will be in the order by time, latitude, and longitude.
   2.1 By sorting, it will return 2 new csv file, 1 with the index of time, latitude, and longitude, and 1 with just the variable data.
   2.2 Sorted file with index will be used for labeling,
   2.3 Sorted file with just the variables will be used for training the models.
3. Run the 'Final Model.py' to create the models.
   3.1 Run it by using the csv containing the variable data, and the label that has been created.
   3.2 The data then normalized using MinMax Normalizer.
   3.3 And then reshaped to its original shape from NetCDF to ensures more effective runtime.
   3.4 The data then splitted into train and test dataset.
   3.5 The models here is using Convolutional layers without flattening to ensures the output data stays the same as the input data.
   3.6 The models then compiled using adam optimizers, and SparseCategoricalCrossentropy loss
   3.7 The models is fitted with the data for training.
   3.8 Then the models will be saved into .keras and .h5 format

# Transforming and cleaning Himawari-8 Data to make label for ERA-5 data parameter
  For labeling, we use data from Himawari-8 satellite.

language used: pyhon
modul used:
pandas
os
numpy
netCDF4
csv

There are few step to get the label from Himawari-8

1. Combining csv

  Use combine_csv.py script to combine all the data inside the Wildfire_Prediction_System\Scripts\Machine Learning Paths\Data Filtering\csv_folder
  This will output a file named "combined_data.csv"

2. Filtering the data

  Use csv_filter.py script to filter the data to only the coordinate included for the project. This will yield file named "filtered_data.csv"

3. Strip the unused column

  We only need the time, year, month, day, latitude, longitude, and heat_level column. Use strip_column.py script to dispose all the unused column. the output of will be a file named "stripped_data.csv"

4.  Change the format of the time column

  Use time_sync.py to combine the time, year, month, and day column into 1 column. and use time_format_fix.py script to change it to correct format.

5. Extract the latitude and longitude from ERA-5 data

  Using the extrace_lan_lon.py script, extract the usable format of latitude and longitude from ERA-5 data

6. Sync the coordinate in the himawari data

  Use coordinate_sync.py to sync the format on the himawari data into the coordinate used in the ERA-5 data. The output will be a file named "rounded_coordinates.csv"

7. clean the duplicates data

  Use remove_duplicates.py script to remove any duplicates data

8. join the data and extract the label

  You can use either csv_join.py if you want to join the era-5 data with the label from the himawari data, or you can use csv_make_label.py which does the same thing, but only output the label column. This will yield a file named "label.csv"
