from pyld import jsonld
import json

doc =    {
        "@type": "wd:Q2188189", #???
        "@id": "simssadb_musical_work:8",
        "P1476": "Salve regina VI",
        "P86": "wd:Q370540",
        "P214": "265244429",
        "P136": "wd:Q3424719",
        "database": "simssadb",
        "files": [
            {   "@type": "simssadb_file", #???
                "@id": "simssadb_file:10",
                "P2701": "wd:Q10610388",
                "P2699": "https://db.simssa.ca/files/10",
                "Last_Pitch": "[43.0]"
            },
            {   "@type": "simssadb_file", #???
                "@id": "simssadb_file:10",
                "P2701": "wd:Q10610388",
                "P2699": "https://db.simssa.ca/files/10",
                "Last_Pitch": "[43.0]"
            }
        ]
    }

context = {
        "simssadb":"https://db.simssa.ca/",
        "simssadb_musical_work": "simssadb:musicalworks/",
        "simssadb_file" : "simssadb:files/",
        "P1476": "wdt:P1476", #title
        "P86": "wdt:P86" , #composer
        "P214": "wdt:P214", #viaf id
        "P136": "wdt:P136",#genre
        "database": "simssadb",
        "P2701": "wdt:P2701", #file type
        "P2699":"wdt:P2699", #url
        "Last_Pitch": "[43.0]",
        "wd": "http://www.wikidata.org/entity/",
        "wdt": "http://www.wikidata.org/prop/direct/"
        
        
}

tested = {"@context" : {
                "simssadb":"https://db.simssa.ca/",
        "mw": "simssadb:musicalworks/",
        "simssadb_file" : "simssadb:files/",
        "P1476": "wdt:P1476", 
        "P86": "wdt:P86" , 
        "P214": "wdt:P214", 
        "P136": "wdt:P136",
        "database": "https://schema.org/Dataset",
        "P2701": "wdt:P2701" ,
  		"P2699":"wdt:P2699", 
        "wd": "http://www.wikidata.org/entity/",
        "wdt": "http://www.wikidata.org/prop/direct/",
  		"files":"simssadb_file"
	},
    "database": "simssadb",
    "@type": "wd:Q2188189",
    "@id": "mw:383",
    "P86": {
        "@id": "wd:Q317937",
        "P214": None
    },
    "P1476": "['Faulx mesdisans']",
    "P136": "wd:Q3424719",
    "files": [
        {
            "@type": "simssadb_file",
            "@id": "https://db.simssa.ca/files/725",
            "P2701": "wd:Q10610388",
            "Last_Pitch": "[41.0]"
        }
    ]}

print(jsonld.expand(tested))