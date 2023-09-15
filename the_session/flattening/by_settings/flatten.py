import pandas as pd

# Define the file paths for each CSV file
csv_files = {
    'tunes': 'tunes.csv',
    'popularity': 'tune_popularity.csv',
    'recordings': 'recordings.csv',
    'aliases': 'transformed/flatten_aliases.csv'
}

# Load each CSV file into a DataFrame
dfs = {}
for table_name, file_path in csv_files.items():
    df = pd.read_csv(f'../data/{file_path}')
    df.columns = [table_name + '_' + col if col != 'tune_id' else col for col in df.columns]
    dfs[table_name] = df

dfs['tunes'] = dfs['tunes'].head(100)

# Merge tables with foreign key relationships
merged_df = pd.merge(dfs['popularity'], dfs['tunes'], on='tune_id', how='right')
merged_df = pd.merge(merged_df, dfs['recordings'], on='tune_id', how='left')
merged_df = pd.merge(merged_df, dfs['aliases'], on='tune_id', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merge_on_settings.csv', index=False)