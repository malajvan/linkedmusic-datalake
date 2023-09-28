from pyld import jsonld
import json

        
tested =   [    
    {
        "musical_work_variant_titles": "['Ave Maria gratia plena \u2026 virgo serena']",
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/add_original_content/simssadb/jsonld/context.jsonld",
        "database": "simssadb:",
        "@type": "wd:Q2188189",
        "@id": "mw:78",
        "composer": {
            "@id": "wd:Q143100",
            "name": "des Prez Josquin"
        },
        "genre_style": {
            "@id": "wd:Q4692",
            "name": "Renaissance"
        },
        "files": [
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/309",
                "file_format": {
                    "@id": "wd:Q2115",
                    "name": "xml"
                },
                "Last_Pitch_Class": "[0.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/310",
                "file_format": {
                    "@id": "wd:Q10610388",
                    "name": "midi"
                },
                "Last_Pitch_Class": "[0.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/311",
                "file_format": {
                    "@id": "wd:Q42332",
                    "name": "pdf"
                },
                "Last_Pitch_Class": None
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/312",
                "file_format": {
                    "@id": "wd:Q27967347",
                    "name": "sibelius"
                },
                "Last_Pitch_Class": None
            }
        ]
    }
]
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))