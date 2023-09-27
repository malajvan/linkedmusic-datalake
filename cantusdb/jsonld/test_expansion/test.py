from pyld import jsonld
import json

        
link_doc =     [
    {
        "incipit": "Fidelia omnia mandata ejus confirmata ",
        "finalis": "E",
        "composer": "wd:Q4233718",
        "absolute_url": "https://cantusdatabase.org/chant/561262",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/new_context/cantusdb/jsonld/context.jsonld"
        ],
        "@id": "chant:561262",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "genre": "wd:Q582093",
        "mode_name": "wd:Q1641387",
        "source": "https://cantusdatabase.org/source/123756",
        "cantus_id": "https://cantusindex.org/id/002865"
    },
    {
        "incipit": "Mulieres sedentes ad monumentum lamentabantur ",
        "finalis": "D",
        "composer": "wd:Q4233718",
        "absolute_url": "https://cantusdatabase.org/chant/562284",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/new_context/cantusdb/jsonld/context.jsonld"
        ],
        "@id": "chant:562284",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "genre": "wd:Q582093",
        "mode_name": "wd:Q960729",
        "source": "https://cantusdatabase.org/source/123756",
        "cantus_id": "https://cantusindex.org/id/003826"
    },
    {
        "incipit": "Verumtamen justi confitebuntur nomini tuo ",
        "finalis": "D",
        "composer": "wd:Q4233718",
        "absolute_url": "https://cantusdatabase.org/chant/670160",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/new_context/cantusdb/jsonld/context.jsonld",
            {
                "genre": "wdt:P136"
            }
        ],
        "@id": "chant:670160",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "genre": "Tract verse",
        "mode_name": "wd:Q842766",
        "source": "https://cantusdatabase.org/source/669907",
        "cantus_id": "https://cantusindex.org/id/g02431j"
    }
]
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(link_doc), indent=2))

