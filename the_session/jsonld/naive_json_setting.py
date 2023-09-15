import pandas as pd
import json

df = pd.read_csv('../flattening/by_settings/merge_on_settings.csv')
float_columns = df.select_dtypes(include=['float']).columns

# Convert float columns to int using pd.Int64Dtype()
df[float_columns] = df[float_columns].astype(pd.Int64Dtype(), errors='ignore')



json_data = df.to_json(orient='records')
parsed_json = json.loads(json_data)
cleaned_json = [{k: v for k, v in record.items() if v is not None} for record in parsed_json]
pretty_json = json.dumps(cleaned_json, indent=4)


with open('settings_naive.json', 'w') as json_file:
    json_file.write(pretty_json)










