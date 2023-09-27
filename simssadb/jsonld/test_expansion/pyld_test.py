from pyld import jsonld
import json

        
tested =   [    {
        "musical_work_variant_titles": "['\u039f passi sparsi \u03bf pensier vaghi et pronti']",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/new_context/simssadb/jsonld/context.jsonld"
        ],
        "database": "simssadb:",
        "@type": "wd:Q2188189",
        "@id": "mw:25",
        "composer": "wd:Q7442579",
        "genre_style": "wd:Q4692",
        "files": [
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/100",
                "file_format": "wd:Q27967347",
                "Last_Pitch_Class": None
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/97",
                "file_format": "wd:Q2115",
                "Last_Pitch_Class": "[9.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/98",
                "file_format": "wd:Q10610388",
                "Last_Pitch_Class": "[9.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/99",
                "file_format": "wd:Q42332",
                "Last_Pitch_Class": None
            }
        ]
    },
    {
        "musical_work_variant_titles": "['Amor quando fioriva mia speme']",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/new_context/simssadb/jsonld/context.jsonld"
        ],
        "database": "simssadb:",
        "@type": "wd:Q2188189",
        "@id": "mw:26",
        "composer": "wd:Q7442579",
        "genre_style": "wd:Q4692",
        "files": [
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/101",
                "file_format": "wd:Q2115",
                "Last_Pitch_Class": "[9.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/102",
                "file_format": "wd:Q10610388",
                "Last_Pitch_Class": "[9.0]"
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/103",
                "file_format": "wd:Q42332",
                "Last_Pitch_Class": None
            },
            {
                "@type": "simssadb_file",
                "@id": "https://db.simssa.ca/files/104",
                "file_format": "wd:Q27967347",
                "Last_Pitch_Class": None
            }
        ]
    }]
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))