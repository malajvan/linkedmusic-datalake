import csv
import pandas as pd

df = pd.read_csv("../reconciliation/reconciled_WikiID.csv")
cols = ['musical_work_id','musical_work_variant_titles','contributor_role','contributor_full_name','contributor_auth_url','contributor_viaf_id', 'genre_style', 'file_format','url_to_file', 'Last_Pitch']
df2 = df[cols]
df2 = df2[df2['contributor_role']== 'COMPOSER'].head(1000)

df2['musical_work_id'] =df2['musical_work_id'].astype(int)



merge_on = ["musical_work_id",'musical_work_variant_titles','contributor_role','contributor_full_name','contributor_auth_url','contributor_viaf_id', 'genre_style']

df2['test_count'] = df2.groupby("musical_work_id").cumcount() + 1
df2 = df2.pivot(index=merge_on, columns='test_count', values=['file_format','url_to_file', 'Last_Pitch'])

# Flatten the multi-index columns
df2.columns = [f'{col[0]}_{col[1]}' for col in df2.columns]

# Reset the index
df2 = df2.reset_index()
del df2['contributor_role'] 


# Display the result
df2.to_csv('./short_rec.csv', index=False)
