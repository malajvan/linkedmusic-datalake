import requests
import json
import musicbrainzngs as mbz 
mbz.set_useragent("YourApp/1.0.0", "1.0.0")
# urls = [
#     #overlap the session
#     'https://musicbrainz.org/ws/2/release-group/cb5877ee-65dd-4968-aa98-b883826274d2', #cooleys reels
#     'https://musicbrainz.org/ws/2/release-group/9939251d-839c-4a0c-bd0c-5ae224e7fcb9', #just piping
#     #overlap simssadb
#     "https://musicbrainz.org/ws/2/release-group/70bc241d-ef99-4edf-9b08-444e2dc434f6", #ave maria by sue ann pinner
#     "https://musicbrainz.org/ws/2/release/cd5d7022-84e0-4ba2-86aa-9272dec2f210/disc/1#f4d5d16c-5a91-4fb6-a8bf-e0461089b67f", #alpine airs: music of switzerland, 13th-16th centuries

#     #overlap cantusdb
#     "https://musicbrainz.org/ws/2/release-group/5fa7b8fc-d600-4b32-8095-d2d132b00658", # renaissance masterpieces
#     "https://musicbrainz.org/ws/2/release-group/df9c1b47-ce5d-4575-a35b-a9e3f5f1250f", #croisade

#     #random ones
#     "https://musicbrainz.org/ws/2/release-group/c2ee4be6-8e36-3fe3-80fe-e207ea88cdc4", #julie is her name - julie london
#     "https://musicbrainz.org/ws/2/release-group/1baf5f39-e798-4cdb-bff3-c098338fba0d", #debussy, ravel; the philadelphia orchestra,...
#     "https://musicbrainz.org/ws/2/release-group/d2f48ef0-9a77-42bc-95af-89dd0c8452b4", #in rainbows: from the basement - radiohead
#     "https://musicbrainz.org/ws/2/release-group/6cbfe76c-012b-41bb-b6fd-c1bc89267898", #street by street (single) - laufey

# ]

# inc = "releases+artists+url-rels" #info retrieving from musicbrainz'
# json_responses = []
# output_file = "api_data.json"
# for url in urls:
#     response = requests.get(url + f"?inc={inc}&fmt=json")
#     print(url + f"?inc={inc}&fmt=json")
#     if response.status_code == 200:
#         print(response.json())
#         json_data = response.json()
#         json_responses.append(json_data)
#     else:
#         print(f"Failed to fetch data from {url}")

# with open(output_file, "w") as file:
#     json.dump(json_responses, file, indent=2)

# print(f"Data written to {output_file}")



mbids = [
    #overlap the session
    'cb5877ee-65dd-4968-aa98-b883826274d2', #cooleys reels
    '9939251d-839c-4a0c-bd0c-5ae224e7fcb9', #just piping
    #overlap simssadb
    "70bc241d-ef99-4edf-9b08-444e2dc434f6", #ave maria by sue ann pinner

    #overlap cantusdb
    "5fa7b8fc-d600-4b32-8095-d2d132b00658", # renaissance masterpieces
    "df9c1b47-ce5d-4575-a35b-a9e3f5f1250f", #croisade

    #random ones
    "c2ee4be6-8e36-3fe3-80fe-e207ea88cdc4", #julie is her name - julie london
    "1baf5f39-e798-4cdb-bff3-c098338fba0d", #debussy, ravel; the philadelphia orchestra,...
    "d2f48ef0-9a77-42bc-95af-89dd0c8452b4", #in rainbows: from the basement - radiohead
    "6cbfe76c-012b-41bb-b6fd-c1bc89267898", #street by street (single) - laufey

]
incl = ['releases','url-rels','artists','recording-rels']
json_responses = []
output_file = "api_data.json"
for url in mbids:
    response = mbz.get_release_group_by_id(mbids[0],includes=incl)
    json_responses.append(response)

with open(output_file, "w") as file:
    json.dump(json_responses, file, indent=2)

print(f"Data written to {output_file}")
