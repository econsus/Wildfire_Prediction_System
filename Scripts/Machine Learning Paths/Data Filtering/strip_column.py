import pandas as pd

def strip_column(input_file, output_file):
    # Read the CSV file into a DataFrame without considering the first row as header
    df = pd.read_csv(input_file, header=None)
    
    # Select the desired columns
    selected_columns = df.iloc[:, [1, 2, 3, 4, 5, 6, 9]]  # Columns are zero-indexed
    
    # Save the DataFrame with the selected columns to a new CSV file
    selected_columns.to_csv(output_file, index=False, header=False)  # Avoid writing headers to the new file
    
    print("Columns have been stripped and saved to", output_file)

# Specify the input and output file paths
input_file = 'Scripts\Machine Learning Paths\Data Filtering\output\\filtered_data.csv'
output_file = 'Scripts\\Machine Learning Paths\\Data Filtering\\output\\stripped_data.csv'

# Call the function with the input and output file paths
strip_column(input_file, output_file)