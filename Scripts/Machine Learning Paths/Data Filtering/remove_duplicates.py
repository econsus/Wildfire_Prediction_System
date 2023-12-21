import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('time_format_fixed.csv')

# Find the row with the maximum heat level for each unique combination
df_cleaned = df.loc[df.groupby(['time', 'latitude', 'longitude'])['Heat_Level'].idxmax()]

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_file.csv', index=False)
