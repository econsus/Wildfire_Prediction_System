import os
import csv

def filter_csv(input_file_path, output_folder, output_file_name, column1_index, range1_start, range1_end, column2_index, range2_start, range2_end):
    """
    Filter data from a CSV file based on specified ranges in two columns.
    
    Parameters:
    - input_file_path (str): Path to the input CSV file.
    - output_folder (str): Path to the output folder.
    - output_file_name (str): Name of the output CSV file.
    - column1_index (int): Index of the first column (0-based) to filter on.
    - range1_start: The start value of the range for the first column (inclusive).
    - range1_end: The end value of the range for the first column (inclusive).
    - column2_index (int): Index of the second column (0-based) to filter on.
    - range2_start: The start value of the range for the second column (inclusive).
    - range2_end: The end value of the range for the second column (inclusive).
    """
    input_file = os.path.abspath(input_file_path)
    output_file_path = os.path.join(os.path.abspath(output_folder), output_file_name)

    with open(input_file, 'r', newline='') as csv_in, open(output_file_path, 'w', newline='') as csv_out:
        reader = csv.reader(csv_in)
        writer = csv.writer(csv_out)


        # Writing rows that satisfy the filter conditions
        for row in reader:
            try:
                value_column1 = float(row[column1_index])  # Assuming numerical values
                value_column2 = float(row[column2_index])  # Assuming numerical values
                
                # Check both columns for the specified ranges
                if range1_start <= value_column1 <= range1_end and range2_start <= value_column2 <= range2_end:
                    writer.writerow(row)
            except (ValueError, IndexError):
                # Handle cases where the value in the specified columns is not a valid number or the column index is out of range
                pass

# Example usage:
input_file_path = 'Scripts\Machine Learning Paths\Data Filtering\output\combined_output.csv'  # Replace with your input CSV file path
output_folder_path = 'Scripts\Machine Learning Paths\Data Filtering\output'  # Replace with your output folder path
output_file_name = 'filtered_data.csv'  # Replace with your desired output file name
column1_to_filter = 5  # 0-based index for the 6th column
range1_start_value = -11.08  # Replace with your desired start value
range1_end_value = 6.07  # Replace with your desired end value

column2_to_filter = 6  # 0-based index for the 7th column
range2_start_value = 94.8  # Replace with your desired start value
range2_end_value = 140.99  # Replace with your desired end value

filter_csv(input_file_path, output_folder_path, output_file_name, column1_to_filter, range1_start_value, range1_end_value, column2_to_filter, range2_start_value, range2_end_value)
