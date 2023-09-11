from pyld import jsonld
import json

        
tested = {
    "@context":{
    "@context": {
        "simssadb": "https://db.simssa.ca/",
        "mw": "simssadb:musicalworks/",
        "simssadb_file": "simssadb:files/",
        "P1476": "wdt:1476",
        "P86": {
            "@id": "wdt:P86",
            "@type": "@id"
        },
        "P214": "wdt:P214",
        "P136": {
            "@id": "wdt:P136",
            "@type": "@id"
        },
        "database": {"@id":"https://schema.org/Dataset",
                     "@type":"@id"},
        "P2701": {
            "@id": "wdt:P2701",
            "@type": "@id"
        },
        "P2699": "wdt:P2699",
        "P5426": "wdt:P5426",
        "wd": "http://www.wikidata.org/entity/",
        "wdt": "http://www.wikidata.org/prop/direct/",
        "files": "simssadb_file"
    }
},
        "database": "simssadb:",
        "@type": "wd:Q2188189",
        "@id": "mw:607",
        "P86": {
            "@id": "wd:Q2920493",
            "P214": "76504834"
        },
        "P1476": "['Son io donna (2) qual mostri ogni tuo bene']",
        "P136": "wd:Q3424719",
        "files": [
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/1592",
                "P2701": "wd:Q10610388",
                "Last_Pitch_Class": "[0.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/1593",
                "P2701": "wd:Q42332",
                "Last_Pitch_Class": None
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/1594",
                "P2701": "wd:Q27967347",
                "Last_Pitch_Class": None
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/1591",
                "P2701": "wd:Q2115",
                "Last_Pitch_Class": "[0.0]"
            }
        ]
    }
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))