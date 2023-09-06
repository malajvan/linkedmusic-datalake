import pandas as pd
import json

df = pd.read_csv('./short_rec.csv')
json_data = df.to_json(orient='records')
parsed_json = json.loads(json_data)
# pretty_json = json.dumps(parsed_json, indent=4)
# with open('gen_json.json', 'w') as json_file:
#     json_file.write(pretty_json)


json_keys = [
    "file_format_1", "file_format_2", "file_format_3", "file_format_4",
    "url_to_file_1", "url_to_file_2", "url_to_file_3", "url_to_file_4",
    "Last_Pitch_1", "Last_Pitch_2", "Last_Pitch_3", "Last_Pitch_4"
]

# Create a nested list of dictionaries


for work in parsed_json:
    work['database'] = 'simssadb'
    nested_list = []
    for i in range(1, 5):
        file_format_key = f"file_format_{i}"
        url_key = f"url_to_file_{i}"
        last_pitch_key = f"Last_Pitch_{i}"
        
        file_format = work.get(file_format_key, None)
        url = work.get(url_key, None)
        last_pitch = work.get(last_pitch_key, None)
        if url is None:
            continue
        nested_list.append({
            'P2701': file_format,
            'url': url,
            'Last_Pitch': last_pitch
        })
    work['files'] = nested_list
    for col in json_keys:
        del work[col]
    
# Print the nested list of dictionaries
pretty_json = json.dumps(parsed_json, indent=4)
with open('nested.json', 'w') as json_file:
    json_file.write(pretty_json)






