import requests
import json

http = requests.Session()
reconciliation_endpoint = 'https://wikidata.reconci.link/en/api'

query_string = '''{
    "@id": {
        "query": "Michele Pesenti",
        "type": "Q5",
        "limit": 5,
        "type_strict": "all",
        "properties":[
        {
        "pid":"P106",
        "v":["composer","singer"]
        },
        {"pid":"P27",
        "v": "Italy"}
        ]
      }
}'''

payload = {'queries': query_string}

response = http.post(reconciliation_endpoint, data=payload)
print(json.dumps(response.json(), indent=2))