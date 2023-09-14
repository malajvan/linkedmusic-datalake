import pandas as pd
import json

df = pd.read_csv('../flattening/final_merged.csv')
json_data = df.to_json(orient='records')
parsed_json = json.loads(json_data)
cleaned_json = [{k: v for k, v in record.items() if v is not None} for record in parsed_json]
pretty_json = json.dumps(cleaned_json, indent=4)


with open('gen_json.json', 'w') as json_file:
    json_file.write(pretty_json)


def group_index(names, record):
    rec = {}
    
    for name in names:
        l = []

        for key, value in record.items():
            parts = key.split('_')
            
            # Check if the key matches the "name_..._#" pattern
            if parts[-1].isdigit() and parts[0] == name:
                index = parts[-1]
                found = False

                # Check if the index already exists in the list
                for s in l:
                    if list(s)[0].split('_')[-1] == index:
                        s[key] = value
                        found = True
                        break
                
                # If the index doesn't exist, create a new dictionary
                if not found:
                    l.append({key: value})
                
            # If the key isn't an indexed name, add it to the result directly
            elif not (parts[-1].isdigit() and parts[0] in names):
                rec[key] = value

        # Add the list to the result under the name key
        rec[name] = l
    
    return rec



grouped_json=[]
names = ['tunes', 'recordings']
for record in cleaned_json:
    grouped_json.append(group_index(names, record)) #grouping indexed as a nested json doc/list

    
pretty_json = json.dumps(grouped_json, indent=4)
with open('compact.jsonld', 'w') as json_file:
    json_file.write(pretty_json)






