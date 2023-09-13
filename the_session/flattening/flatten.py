import pandas as pd

# Define the file paths for each CSV file
csv_files = {
    'tunes': 'flatten_tunes.csv',
    'tune_popularity': 'tune_popularity.csv',
    'recordings': 'recordings.csv',
    'aliases': 'flatten_aliases.csv'
}

# Load each CSV file into a DataFrame
dfs = {}
for table_name, file_path in csv_files.items():
    dfs[table_name] = pd.read_csv(f'data/{file_path}')

dfs['tunes'] = dfs['tunes'].head(100)

# Merge tables with foreign key relationships
merged_df = pd.merge(dfs['tune_popularity'], dfs['tunes'], on='tune_id', how='right')
merged_df = pd.merge(merged_df, dfs['recordings'], on='tune_id', how='left')
merged_df = pd.merge(merged_df, dfs['aliases'], on='tune_id', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)

print('Merged data saved to merged_data.csv')

df = pd.read_csv('merged_data.csv')
merged_on =['tune_id'] 

df['index_suffix'] = df.groupby(merged_on).cumcount() + 1
# print(df.groupby(merged_on).describe())

# # Pivot the DataFrame based on 'index_suffix' and create separate columns for each attribute
pivot_table = df.pivot(index=merged_on, columns='index_suffix', values=['id', 'artist', 'recording', 'track', 'number'])

# # Flatten the multi-level column index
pivot_table.columns = [f'{col[0]}_{col[1]}' for col in pivot_table.columns]

# # Reset the index to make 'index_suffix' a regular column
pivot_table.reset_index(inplace=True)


pivot_table.to_csv('testy.csv', index=False)
