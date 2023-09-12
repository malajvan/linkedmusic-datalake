from pyld import jsonld
import json

        
tested =     {
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/simssadb/jsonld/context.jsonld",
        "database": "simssadb:",
        "@type": "wd:Q2188189",
        "@id": "mw:4",
        "P86": {
            "@id": "wd:Q2920493",
            "P214": "76504834"
        },
        "P1476": "['Son io donna qual mostri ogni tuo bene']",
        "P136": "wd:Q4692",
        "files": [
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/13",
                "P2701": "wd:Q2115",
                "Last_Pitch_Class": "[2.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/14",
                "P2701": "wd:Q10610388",
                "Last_Pitch_Class": "[2.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/15",
                "P2701": "wd:Q42332",
                "Last_Pitch_Class": None
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/16",
                "P2701": "wd:Q27967347",
                "Last_Pitch_Class": None
            }
        ]
    }
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))