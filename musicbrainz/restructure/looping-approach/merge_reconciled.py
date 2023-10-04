import json
import pandas as pd

with open('extracted_ids.csv','r') as f:
    id_table = pd.read_csv(f)

with open('../../data/initial_compact.jsonld','r') as f:
    data = json.load(f)

def merge_ids(data, valid_formats):
    if isinstance(data, dict):
        for key, value in data.items():
            # if key == '@id' and any(value.startswith(format) for format in valid_formats):
            #     ids.add(value)
            if key == 'genre':
                for i in range(len(data['genre'])):
                    replacements = {'@id': id_table[id_table['@id']==data['genre'][i]]['sameAs'],
                                    'name':id_table[id_table['@id']==data['genre'][i]]['name']}
                    if data['genre'][i] in replacements:
                        data['genre'][i] = replacements[data['genre'][i]]
            else:
                merge_ids(value, valid_formats)  # Pass valid_formats as well
    elif isinstance(data, list):
        for item in data:
            merge_ids(item, valid_formats)  # Pass valid_formats as well
    return data

output=merge_ids(data, [])
with open('compact.jsonld', 'w', newline='') as json_file:
    json.dump(output, json_file, indent=2)

print('CSV file created with @id values.')
