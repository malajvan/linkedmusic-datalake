import pandas as pd

# Define the file paths for each CSV file
csv_files = {
    'tunes': 'transformed/flatten_tunes.csv',
    'tune_popularity': 'tune_popularity.csv',
    'recordings': 'recordings.csv',
    'aliases': 'transformed/flatten_aliases.csv'
}

# Load each CSV file into a DataFrame
dfs = {}
for table_name, file_path in csv_files.items():
    df = pd.read_csv(f'data/{file_path}')
    df.columns = [table_name + '_' + col if col != 'tune_id' else col for col in df.columns]
    dfs[table_name] = df

dfs['tunes'] = dfs['tunes'].head(100)

# Merge tables with foreign key relationships
merged_df = pd.merge(dfs['tune_popularity'], dfs['tunes'], on='tune_id', how='right')
# merged_df = pd.merge(merged_df, dfs['recordings'], on='tune_id', how='left')
no_recording = pd.merge(merged_df, dfs['aliases'], on='tune_id', how='left')

# Save the merged DataFrame to a new CSV file
no_recording.to_csv('no_recordings_merge.csv', index=False)

print('Merged data saved to no_recordings.csv')
merged_on=['tune_id']
with_recording = pd.merge(no_recording, dfs['recordings'], on='tune_id', how='left')

with_recording['index_suffix'] = with_recording.groupby(merged_on).cumcount() + 1
# print(with_recording.groupby(merged_on).describe())

# # Pivot the DataFrame based on 'index_suffix' and create separate columns for each attribute
pivot_table = with_recording.pivot(index=merged_on, columns='index_suffix', values=['recordings_id', 'recordings_artist', 'recordings_recording', 'recordings_track', 'recordings_number'])

# # Flatten the multi-level column index
pivot_table.columns = [f'{col[0]}_{col[1]}' for col in pivot_table.columns]

# # Reset the index to make 'index_suffix' a regular column
pivot_table.reset_index(inplace=True)


pivot_table.to_csv('data/transformed/flatten_recordings.csv', index=False)
# print(pivot_table.columns)\
final = pd.merge(no_recording, pivot_table, on="tune_id", how="left")
final.to_csv("final_merged.csv",index=False)