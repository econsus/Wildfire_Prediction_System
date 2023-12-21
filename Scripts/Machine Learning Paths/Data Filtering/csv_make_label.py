import pandas as pd
from tqdm import tqdm

# Load the CSV files into pandas DataFrames
df1 = pd.read_csv('sorted_sshf.csv')
df2 = pd.read_csv('cleaned_file.csv')
print("Finished reading the CSV files\n")

# Perform a left join using three variables
merged_df = pd.merge(df1, df2, on=['time', 'latitude', 'longitude'], how='left')

# Fill missing values in the new column with 0
merged_df['Heat_Level'] = merged_df['Heat_Level'].fillna(0).astype(int)
print("Files have been merged\n")

# Keep only the 'Heat_Level' column
result_df = merged_df[['Heat_Level']]

# Save the result to a new CSV file
result_df.to_csv('label.csv', index=False)
print("Result CSV with only 'Heat_Level' column has been saved\n")
