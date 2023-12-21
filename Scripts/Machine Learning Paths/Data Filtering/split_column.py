import csv

# Specify the path to your input CSV file
input_csv_path = 'output/stripped_data.csv'

# Specify the paths for the output CSV files
output_csv_path_1_4 = 'output/output_file_1_4.csv'
output_csv_path_5_7 = 'path/to/your/output_file_5_7.csv'

# Open the input CSV file in read mode
with open(input_csv_path, 'r') as input_file:
    # Create a CSV reader object
    csv_reader = csv.reader(input_file)

    # Read the header
    header = next(csv_reader)

    # Indices of columns to extract
    indices_1_4 = [0, 1, 2, 3]
    indices_5_7 = [4, 5, 6]

    # Create CSV writers for output files
    with open(output_csv_path_1_4, 'w', newline='') as output_file_1_4:
        csv_writer_1_4 = csv.writer(output_file_1_4)
        csv_writer_1_4.writerow(header[:4])  # Write the header for columns 1-4
        for row in csv_reader:
            csv_writer_1_4.writerow([row[i] for i in indices_1_4])

    # Move the file cursor back to the beginning of the input CSV file
    input_file.seek(0)

    # Skip the header in the second pass
    next(csv_reader)

    with open(output_csv_path_5_7, 'w', newline='') as output_file_5_7:
        csv_writer_5_7 = csv.writer(output_file_5_7)
        csv_writer_5_7.writerow(header[4:])  # Write the header for columns 5-7
        for row in csv_reader:
            csv_writer_5_7.writerow([row[i] for i in indices_5_7])
