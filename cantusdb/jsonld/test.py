from pyld import jsonld
import json

        
link_doc =     [
   {
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld"
        ],
        "@id": "chant:670569",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wd:Q4233718",
        "P1922": "Colligite primum zizania et alligate ",
        "P136": "wd:Q582093",
        "Q731978": "wd:Q960729",
        "Q4484726": "D",
        "source": "https://cantusdatabase.org/source/669163",
        "cantus_id": "https://cantusindex.org/id/001853"
    },
    {
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld",
            {
                "P136": "wdt:P136"
            }
        ],
        "@id": "chant:670191",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wd:Q4233718",
        "P1922": "Sicut imber super gramen  et ",
        "P136": "Tract verse",
        "Q731978": "wd:Q57976142",
        "Q4484726": "G",
        "source": "https://cantusdatabase.org/source/669907",
        "cantus_id": "https://cantusindex.org/id/g02373b.1"
    }
]
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(link_doc), indent=2))

