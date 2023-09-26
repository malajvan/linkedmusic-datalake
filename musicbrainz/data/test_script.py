import json
flattened_data = [
    {
      "_ - @id" : "http://musicbrainz.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd",
      "_ - @type" : "MusicRelease",
      "_ - @context" : "https://schema.org/docs/jsonldcontext.json",
      "_ - name" : "McGreevy & Cooley",
      "_ - musicReleaseFormat" : "http://schema.org/VinylFormat",
      "_ - creditedTo" : "Johnny McGreevy & Séamus Cooley",
      "_ - duration" : None,
      "_ - catalogNumber" : "PH 2005",
      "_ - inLanguage" : None,
      "_ - sameAs" : "https://www.amazon.com/gp/product/B001RF74KG",
      "_ - gtin14" : None,
      "_ - track - _ - name" : "The Broken Pledge / Julia Delaney (reels)",
      "_ - track - _ - @id" : "http://musicbrainz.org/recording/d506fa4b-733e-4864-8b41-29c5c510024e",
      "_ - track - _ - trackNumber" : "1.1",
      "_ - track - _ - @type" : "MusicRecording",
      "_ - track - _ - duration" : None,
      "_ - track - _ - isrcCode" : None,
      "_ - track - _ - sameAs" : None,
      "_ - track - _ - sameAs - sameAs" : None,
      "_ - track - _ - contributor - _ - @type" : None,
      "_ - track - _ - contributor - _ - roleName" : None,
      "_ - track - _ - contributor - _ - contributor - @id" : None,
      "_ - track - _ - contributor - _ - contributor - name" : None,
      "_ - track - _ - contributor - _ - contributor - @type" : None,
      "_ - track - _ - contributor - _ - contributor - @type - @type" : None,
      "_ - track - _ - contributor - _ - roleName - roleName" : None,
      "_ - track - _ - recordingOf - @id" : None,
      "_ - track - _ - recordingOf - @type" : None,
      "_ - track - _ - recordingOf - name" : None,
      "_ - track - _ - recordingOf - sameAs" : None,
      "_ - track - _ - recordingOf - sameAs - sameAs" : None,
      "_ - track - _ - producer - name" : None,
      "_ - track - _ - producer - @id" : None,
      "_ - track - _ - producer - @type - @type" : None,
      "_ - track - _ - producer - _ - @id" : None,
      "_ - track - _ - producer - _ - name" : None,
      "_ - track - _ - producer - _ - @type - @type" : None,
      "_ - track - _ - isrcCode - isrcCode" : None,
      "_ - image - encodingFormat" : "jpg",
      "_ - image - representativeOfPage" : "True",
      "_ - image - @type" : "ImageObject",
      "_ - image - contentUrl" : "//coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341.jpg",
      "_ - image - thumbnail - _ - encodingFormat" : "jpg",
      "_ - image - thumbnail - _ - contentUrl" : "//coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-250.jpg",
      "_ - image - thumbnail - _ - @type" : "ImageObject",
      "_ - releaseOf - creditedTo" : "Johnny McGreevy & Séamus Cooley",
      "_ - releaseOf - albumProductionType" : "http://schema.org/StudioAlbum",
      "_ - releaseOf - @type" : "MusicAlbum",
      "_ - releaseOf - albumReleaseType" : "http://schema.org/AlbumRelease",
      "_ - releaseOf - @id" : "http://musicbrainz.org/release-group/cb5877ee-65dd-4968-aa98-b883826274d2",
      "_ - releaseOf - name" : "McGreevy & Cooley",
      "_ - releaseOf - byArtist - @id" : None,
      "_ - releaseOf - byArtist - name" : None,
      "_ - releaseOf - byArtist - @type" : None,
      "_ - releaseOf - byArtist - _ - name" : "Johnny McGreevy",
      "_ - releaseOf - byArtist - _ - @id" : "http://musicbrainz.org/artist/de8f8c4b-a768-460f-ae9e-1ca8bbaf426f",
      "_ - releaseOf - byArtist - _ - @type" : None,
      "_ - releaseOf - byArtist - _ - @type - @type" : "Person",
      "_ - releaseOf - byArtist - @type - @type" : None,
      "_ - hasReleaseRegion - _ - releaseDate" : "1974",
      "_ - hasReleaseRegion - _ - @type" : "CreativeWorkReleaseRegion",
      "_ - hasReleaseRegion - _ - releaseCountry - @id" : "http://musicbrainz.org/area/489ce91b-6658-3307-9877-795b68554c98",
      "_ - hasReleaseRegion - _ - releaseCountry - name" : "United States",
      "_ - hasReleaseRegion - _ - releaseCountry - @type" : "Country",
      "_ - recordLabel - @id" : "http://musicbrainz.org/label/d476b74d-670d-44ab-be5c-2c17caea20a9",
      "_ - recordLabel - name" : "Philo",
      "_ - recordLabel - @type" : "MusicLabel",
      "_ - recordLabel - _ - @type" : None,
      "_ - recordLabel - _ - @id" : None,
      "_ - recordLabel - _ - name" : None,
      "_ - catalogNumber - catalogNumber" : None,
      "_ - sameAs - sameAs" : None,
      "_ - genre - genre" : None,
      "_ - producer - @id" : None,
      "_ - producer - name" : None,
      "_ - producer - @type - @type" : None
    }
]
nested_json = {}
for i in flattened_data:
    for key, value in i.items():
        key = key.replace('_ - ','')
        keys = key.split(" - ")  # Split the key into nested levels
        current_level = nested_json
        for k in keys[:-1]:
            current_level = current_level.setdefault(k, {})
        if value is not None:
            current_level[keys[-1]] = value

# Convert the nested JSON structure to a JSON string


# Print the reconstructed nested JSON
with open('test_output.json', 'w') as file:
    json.dump(nested_json, file, indent=2)