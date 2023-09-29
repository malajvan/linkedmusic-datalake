from pyld import jsonld
import json

        
link_doc =     [
    {
        "incipit": "Judica causam meam defende quia ",
        "finalis": "G",
        "absolute_url": "https://cantusdatabase.org/chant/562072",
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld",
        "@id": "chant:562072",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "composer": {
            "@id": "wd:Q4233718",
            "name": "Anonymous"
        },
        "genre": {
            "@id": "wd:Q582093",
            "name": "Antiphon"
        },
        "mode_name": {
            "@id": "wd:Q57976142",
            "name": "hypomixolydian"
        },
        "source": "https://cantusdatabase.org/source/123756",
        "cantus_id": "https://cantusindex.org/id/003515"
    },
    {
        "incipit": "Ex Sion species decoris ejus ",
        "finalis": "E",
        "absolute_url": "https://cantusdatabase.org/chant/560594",
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/add_original_content/cantusdb/jsonld/context.jsonld",
        "@id": "chant:560594",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "composer": {
            "@id": "wd:Q4233718",
            "name": "Anonymous"
        },
        "genre": "Responsory verse",
        "source": "https://cantusdatabase.org/source/123756",
        "cantus_id": "https://cantusindex.org/id/006393a"
    }
]
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(link_doc), indent=2))

