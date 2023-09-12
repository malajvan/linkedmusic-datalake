import pandas as pd

# Define the file paths for each CSV file
csv_files = {
    'tunes': 'tunes.csv',
    'sets': 'sets.csv',
    'tune_popularity': 'tune_popularity.csv',
    'sessions': 'sessions.csv',
    'recordings': 'recordings.csv',
    'events': 'events.csv',
    'aliases': 'aliases.csv'
}

# Load each CSV file into a DataFrame
dfs = {}
for table_name, file_path in csv_files.items():
    dfs[table_name] = pd.read_csv(f'the_session/TheSession-data/csv/{file_path}')

# Merge tables with foreign key relationships
merged_df = pd.merge(dfs['tune_popularity'], dfs['tunes'], on='tune_id', how='inner')
merged_df = pd.merge(merged_df, dfs['sets'], on='tune_id', how='inner')
merged_df = pd.merge(merged_df, dfs['sessions'], left_on='area', right_on='area', how='left')
merged_df = pd.merge(merged_df, dfs['recordings'], on='tune_id', how='left')
merged_df = pd.merge(merged_df, dfs['events'], left_on='area', right_on='area', how='left')
merged_df = pd.merge(merged_df, dfs['aliases'], on='tune_id', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)

print('Merged data saved to merged_data.csv')
