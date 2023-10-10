from pyld import jsonld
import json


data = [

  {
    "@id": "http://musicbrainz.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd",
    "recordLabel": {
      "@id": "http://musicbrainz.org/label/d476b74d-670d-44ab-be5c-2c17caea20a9",
      "name": "Philo",
      "@type": "MusicLabel"
    },
    "image": {
      "thumbnail": [
        {
          "encodingFormat": "jpg",
          "contentUrl": "//coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-250.jpg",
          "@type": "ImageObject"
        },
        {
          "@type": "ImageObject",
          "encodingFormat": "jpg",
          "contentUrl": "//coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-500.jpg"
        },
        {
          "@type": "ImageObject",
          "encodingFormat": "jpg",
          "contentUrl": "//coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-1200.jpg"
        }
      ],
      "encodingFormat": "jpg",
      "representativeOfPage": "True",
      "@type": "ImageObject",
      "contentUrl": "//coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341.jpg"
    },
    "@type": "MusicRelease",
    "@context": [
      "https://schema.org/docs/jsonldcontext.json",
      "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/musicbrainz/jsonld/looping-approach/context.jsonld"
    ],
    "releaseOf": {
      "creditedTo": "Johnny McGreevy & S\u00e9amus Cooley",
      "albumProductionType": "http://schema.org/StudioAlbum",
      "@type": "MusicAlbum",
      "albumReleaseType": "http://schema.org/AlbumRelease",
      "@id": "http://musicbrainz.org/release-group/cb5877ee-65dd-4968-aa98-b883826274d2",
      "name": "McGreevy & Cooley",
      "byArtist": [
        {
          "@type": [
            "Person",
            "MusicGroup"
          ],
          "name": "Johnny McGreevy",
          "@id": "http://musicbrainz.org/artist/de8f8c4b-a768-460f-ae9e-1ca8bbaf426f"
        },
        {
          "@type": [
            "Person",
            "MusicGroup"
          ],
          "@id": "http://musicbrainz.org/artist/5439eef7-2d99-4024-9b21-482a4c8550b3",
          "name": "S\u00e9amus Cooley"
        }
      ]
    },
    "name": "McGreevy & Cooley",
    "track": [
      {
        "name": "The Broken Pledge / Julia Delaney (reels)",
        "@id": "http://musicbrainz.org/recording/d506fa4b-733e-4864-8b41-29c5c510024e",
        "trackNumber": "1.1",
        "@type": "MusicRecording"
      },
      {
        "name": "Se\u00e1n sa Ceo / Michael Preston's (reels)",
        "@id": "http://musicbrainz.org/recording/b59c6d66-e6c1-4902-a673-953f84c17577",
        "@type": "MusicRecording",
        "trackNumber": "1.2"
      },
      {
        "@type": "MusicRecording",
        "trackNumber": "1.3",
        "@id": "http://musicbrainz.org/recording/efdbad07-70af-4057-b525-704a94096174",
        "name": "Jimmy Neary's / Jim Ward's (jigs)"
      },
      {
        "@id": "http://musicbrainz.org/recording/bb245713-1178-4891-871a-c98c3a9bf451",
        "name": "Down the Broom / The Gatehouse Maid (reels)",
        "@type": "MusicRecording",
        "trackNumber": "1.4"
      },
      {
        "name": "Sliabh na mBan / Mo Bhuirnin Ban (airs)",
        "@id": "http://musicbrainz.org/recording/3759a5eb-cdc2-4bb7-bd4a-5adc2b71e26e",
        "trackNumber": "1.5",
        "@type": "MusicRecording"
      },
      {
        "name": "Se\u00e1n Ryan's (hornpipes)",
        "@id": "http://musicbrainz.org/recording/cd5fb5ef-b795-4339-8f15-21d0cc452fb3",
        "trackNumber": "1.6",
        "@type": "MusicRecording"
      },
      {
        "@type": "MusicRecording",
        "trackNumber": "1.7",
        "@id": "http://musicbrainz.org/recording/33147eb3-d5b6-4655-b256-42583b25923b",
        "name": "Ginny's Favourite / The Bird in the Bush (reels)"
      },
      {
        "name": "The Reel of Bogie",
        "@id": "http://musicbrainz.org/recording/37a34bbf-2a28-4d0a-a047-9e6589696c03",
        "@type": "MusicRecording",
        "trackNumber": "1.8"
      },
      {
        "@type": "MusicRecording",
        "trackNumber": "1.9",
        "@id": "http://musicbrainz.org/recording/1d04276e-0bbe-4ab5-bde3-507fd05cbd32",
        "name": "The Crooked Road to Dublin / The Moving Bog (reels)"
      },
      {
        "@type": "MusicRecording",
        "trackNumber": "1.10",
        "name": "The Skylark / Roaring Mary (reels)",
        "@id": "http://musicbrainz.org/recording/94a04e93-3702-45fd-9323-aacc38508e1f"
      },
      {
        "name": "The Plains of Boyle / The Boys of Bluehill (hornpipes)",
        "@id": "http://musicbrainz.org/recording/c382d06d-61be-4977-b1d9-a51b2e2d6102",
        "@type": "MusicRecording",
        "trackNumber": "1.11"
      },
      {
        "name": "McGreevy's / Father Kelly's 2 (reels)",
        "@id": "http://musicbrainz.org/recording/c2391cc3-8130-4852-a28a-bfe09184570d",
        "trackNumber": "1.12",
        "@type": "MusicRecording"
      },
      {
        "name": "The Lilting Banshee / The Butcher's March (jigs)",
        "@id": "http://musicbrainz.org/recording/9543c272-fbd8-48d8-ada6-415de1415ef5",
        "@type": "MusicRecording",
        "trackNumber": "1.13"
      },
      {
        "trackNumber": "1.14",
        "@type": "MusicRecording",
        "name": "Ownie Davy's / Money in Both Pockets (reels)",
        "@id": "http://musicbrainz.org/recording/057b6f03-6555-4c25-95e7-2d6f0aee2b6a"
      },
      {
        "@id": "http://musicbrainz.org/recording/3358da5f-d580-40ab-92b0-13b8817d5387",
        "name": "Tim Maloney's / Cooley's (reels)",
        "trackNumber": "1.15",
        "@type": "MusicRecording"
      },
      {
        "@type": "MusicRecording",
        "trackNumber": "1.16",
        "@id": "http://musicbrainz.org/recording/20409b65-c2af-4d5e-b946-f48739863be0",
        "name": "The Chicago / Reidy's (reels)"
      },
      {
        "@type": "MusicRecording",
        "trackNumber": "1.17",
        "name": "The Trip to Vermont (hornpipe)",
        "@id": "http://musicbrainz.org/recording/4f4a4dac-8115-4e3b-95bf-f34cdeeafc81"
      }
    ],
    "musicReleaseFormat": "http://schema.org/VinylFormat",
    "hasReleaseRegion": [
      {
        "releaseDate": "1974",
        "releaseCountry": {
          "@id": "wd:Q30",
          "name": "United States",
          "@type": "Country"
        },
        "@type": "CreativeWorkReleaseRegion"
      }
    ],
    "creditedTo": "Johnny McGreevy & S\u00e9amus Cooley",
    "catalogNumber": "PH 2005",
    "sameAs": "https://www.amazon.com/gp/product/B001RF74KG",
    "database": "https://musicbrainz.org/"
  }]

with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(data), indent=2))