import pandas as pd
'''
flatten_tunes.csv doesn't have abc columns. 
It merge all rows with the same tune_id and name and create new columns with indexes for the subsequent columns
'''


df = pd.read_csv("./data/tunes.csv")
df.drop(['abc'], axis=1)
merge_on = ['tune_id','name']

df['test_count'] = df.groupby(["tune_id",'name']).cumcount() + 1
df2 = df.pivot(index=merge_on, columns='test_count', values=['setting_id', 'type', 'meter', 'mode', 'date','username'])

df2.columns = [f'{col[0]}_{col[1]}' for col in df2.columns]

# Reset the index
df2 = df2.reset_index()


# Display the result
df2.to_csv('data/transformed/flatten_tunes.csv', index=False)