import pandas as pd
from tqdm import tqdm

# Load the CSV files into pandas DataFrames
df1 = pd.read_csv('sshf_csv.csv')
df2 = pd.read_csv('time_format_fixed.csv')
print("finished reading the csv files\n")
# Perform a left join using three variables
merged_df = pd.merge(df1, df2, on=['time', 'latitude', 'longitude'], how='left')

# Fill missing values in the new column with 0
merged_df['Heat_Level'] = merged_df['Heat_Level'].fillna(0).astype(int)
print("Files has been merged \n")
# Get the total number of rows for progress tracking
total_rows = len(merged_df)


# Save the result to a new CSV file
merged_df.to_csv('sshf_only_labeled.csv', index=False)
