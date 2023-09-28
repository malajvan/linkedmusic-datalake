import pandas as pd
import json
import re

# add the path to your reconciled csv to produce the compact jsonld.
# to change the context by :
#       - replace the '@context' key below with another context in the url
#       - make changes to the file 'context.jsonld' and make sure to push the 
#         changes on the appropriate branch (make sure the link below match where you host the context)

df = pd.read_csv('../reconciled_cantus_09202023.csv')
json_data = df.to_json(orient='records')
parsed_json = json.loads(json_data)
# pretty_json = json.dumps(parsed_json, indent=4)
# with open('gen_json.json', 'w') as json_file:
#     json_file.write(pretty_json)




def handle_rec_col(work, val, key, wID):
    if val is None:
        return None
    if re.match(r"^[Q]\d+", val ): #if cell was reconciled with wikidata
        return f"wd:{val}"
    if val[:8]=="https://" : #if cell was reconciled with another source
        return val
    else: #cell is value
        work["@context"].append({key:f"wdt:{wID}"}) # overwrite context
        return val


def create_json_compact(js):
    for work in js:

        work["@context"] = ["https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/new_context/cantusdb/jsonld/context.jsonld"]
        work["@id"] = f"chant:{work.pop('chant_id')}" #the @id of each document should be the link to the chant in its database
        work["@type"] = "wd:Q23072435" #chant

        work['database'] = 'cantusdb:'
        work["composer"] = "wd:Q4233718" #composer anonymous
        # work["P1922"] = work.pop("incipit")

        work["genre"] = handle_rec_col(work,work.pop("genre"), "genre", "P136")


        # work["Q731978"] = f'wd:{work.pop("mode_name")}'
        work["mode_name"] = handle_rec_col(work, work.pop("mode_name"), "mode_name", "Q731978")

        # work["Q4484726"] = work.pop("finalis") #wikidata Final is closest term to finalis

        work["source"] = work.pop("src_link")

        work["cantus_id"] = f"https://cantusindex.org/id/{work.pop('cantus_id')}"
        del work["mode"]

        
        for key in list(work.keys()): #clean up nulls
            if work[key] is None:
                del work[key]
    # Print the nested list of dictionaries
    return json.dumps(js, indent=4)



with open('compact.jsonld', 'w') as json_file:
    json_file.write(create_json_compact(parsed_json))




