import os
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, jsonify
from netCDF4 import Dataset

app = Flask(__name__)

# Load the model (choose either SavedModel or HDF5 format)
model = tf.keras.models.load_model('Final_classification_model.keras')  # Or use 'Test_model_2.h5'

# Define the normalization function outside the predict function
def normalize_series(data, min, max):
    min = np.array(min)
    data = data - min
    data = data / (max - min)
    return data

@app.route('/predict', methods=['POST'])
def predict():
    #data = request.get_json(force=True)  # Get input data as JSON
    data = Dataset('Data 2023.nc')
    # Preprocess the data as needed (matching model's input format)
    data = data.variables[['slhf','sshf']][:]
    data = np.array(data) #.reshape((1, 69, 185, 2))  # Assuming input shape
    data = normalize_series(data, *data.min(axis=0), *data.max(axis=0))  # Use the function for normalization

    # Make prediction using the model
    prediction = model.predict(data)
    #reshape the data to 1D array to get value for every point of coordinate
    prediction = prediction.reshape((len(data)*69*185,4))
    # Process and return the prediction as required
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

