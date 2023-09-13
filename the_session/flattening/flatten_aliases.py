import pandas as pd

df = pd.read_csv("./data/aliases.csv")
'''
# flatten_aliases.csv merge all rows by tune_id and name and create columns for different aliases'''
# merge_on = ['tune_id','name']

# df['test_count'] = df.groupby(["tune_id",'name']).cumcount() + 1
# # df2 = df.pivot(index=merge_on, columns='test_count', values=['alias'])

# df2.columns = [f'{col[0]}_{col[1]}' for col in df2.columns]

# # Reset the index
# df2 = df2.reset_index()

'''
flatten aliases create a list of aliases for each tune_id and name pair
'''
df = df.groupby(['tune_id','name']).agg(tuple).map(list).reset_index()
# Display the result
df.to_csv('data/flatten_aliases.csv', index=False)