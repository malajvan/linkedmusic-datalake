from pyld import jsonld
import json

        
val_doc =     [{
        "volpiano": "1---d--e---f---g--g---g--hg--fg--g---d--f---e--d---d---e7---f---g--g---hhg--f--h---fhf--g---k---j--h---k--l---j--k7--hgf---h--hg--fef--g---e---f--e---d--d---e---f--g--g---hf--hg--f-fG---g77---4",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld",
            {
                "P136": "wdt:P136"
            }
        ],
        "@id": "chant:638102",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wd:Q4233718",
        "P1922": "Ego cum meis sodalibus bene ",
        "P136": "Dramatic element (used for items of liturgical drama that are not otherwise rubricked)",
        "Q731978": "wd:Q57976142",
        "Q4484726": "G",
        "source": "https://cantusdatabase.org/source/588308"
    },
     {
        "volpiano": "1---gh--k--k---lM---n7--m--ml---m--l--jk---l---h--g--g---gh--k--lm---lml---k---kj--h---k7--jk---lkh--g--ghg--g---4",
        "@context": [
            "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld"
        ],
        "@id": "chant:674495",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wd:Q4233718",
        "P1922": "Asperges me domine hyssopo et ",
        "P136": "wd:Q582093",
        "Q731978": "wd:Q321814",
        "Q4484726": "G",
        "source": "https://cantusdatabase.org/source/674494"
    }]
with open('./val_expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(val_doc), indent=2))

