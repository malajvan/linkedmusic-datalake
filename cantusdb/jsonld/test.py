from pyld import jsonld
import json

        
link_doc =     [
       {
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld"
        ],
        "@id": "chant:638175",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wd:Q4233718",
        "P1922": "Ach ach fervens dulcedo absorbuit ",
        "P136": "https://cantusdatabase.org/genre/134",
        "Q731978": "wd:Q842766",
        "Q4484726": "D",
        "source": "https://cantusdatabase.org/source/588308"
    },
    {
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld"
        ],
        "@id": "chant:643323",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wd:Q4233718",
        "P1922": "Confiteantur domino misericordiae ejus et ",
        "P136": "wd:Q849305",
        "Q4484726": "A",
        "source": "https://cantusdatabase.org/source/638308"
    }
]
with open('./link_expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(link_doc), indent=2))

