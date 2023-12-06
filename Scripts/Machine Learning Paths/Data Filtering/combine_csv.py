import os
import pandas as pd

def combine_csv_files(input_folder, output_folder, output_file):
    # Initialize an empty DataFrame to store the combined data
    combined_df = pd.DataFrame()

    # Traverse through the directory tree using os.walk to include files in subdirectories
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.csv'):
                file_path = os.path.join(root, file)
                try:
                    # Read the CSV file using pandas, excluding the first two rows and the first column
                    df = pd.read_csv(file_path, header=None, skiprows=[0, 1], usecols=lambda x: x != 0)
                    # Concatenate the DataFrame to the combined DataFrame
                    combined_df = pd.concat([combined_df, df], ignore_index=True)
                except pd.errors.EmptyDataError:
                    print(f"Empty CSV file: {file_path}")

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Save the combined DataFrame to a new CSV file in the specified output folder
    output_path = os.path.join(output_folder, output_file)
    combined_df.to_csv(output_path, index=False, header=False)

# Example usage:
input_folder = 'Scripts\Machine Learning Paths\Data Filtering\csv_folder'  # Replace with the input directory you want to choose
output_folder = 'Scripts\Machine Learning Paths\Data Filtering\output'  # Replace with the output directory you want to choose
output_file = 'combined_output.csv'
combine_csv_files(input_folder, output_folder, output_file)
