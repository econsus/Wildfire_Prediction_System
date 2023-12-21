import pandas as pd

def change_time_format(csv_file_path, output_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Assuming the time column header is 'time', change its format
    df['time'] = pd.to_datetime(df['time'], format='%Y/%m/%d %H:%M').dt.strftime('%Y-%m-%d %H:%M:00')

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # Replace 'your_input_file.csv' with the path to your input CSV file
    input_file_path = 'rounded_coordinates.csv'

    # Replace 'your_output_file.csv' with the desired path for the output CSV file
    output_file_path = 'time_format_fixed.csv'

    change_time_format(input_file_path, output_file_path)

    print(f"Time format changed and saved to {output_file_path}")
