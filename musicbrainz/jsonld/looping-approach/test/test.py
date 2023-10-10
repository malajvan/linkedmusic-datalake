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
          "contentUrl": {
            "@id": "https://coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-250.jpg"
          },
          "@type": "ImageObject"
        },
        {
          "@type": "ImageObject",
          "encodingFormat": "jpg",
          "contentUrl": {
            "@id": "https://coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-500.jpg"
          }
        },
        {
          "@type": "ImageObject",
          "encodingFormat": "jpg",
          "contentUrl": {
            "@id": "https://coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341-1200.jpg"
          }
        }
      ],
      "encodingFormat": "jpg",
      "representativeOfPage": "True",
      "@type": "ImageObject",
      "contentUrl": {
        "@id": "https://coverartarchive.org/release/20027ad4-6667-49b6-bd07-5ac12d57f8dd/28092634341.jpg"
      }
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
  },
  {
    "hasReleaseRegion": [
      {
        "releaseCountry": {
          "@type": "Country",
          "name": "Ireland",
          "@id": "wd:Q27"
        },
        "releaseDate": "2010",
        "@type": "CreativeWorkReleaseRegion"
      }
    ],
    "creditedTo": "Michael Cooney",
    "inLanguage": "en",
    "catalogNumber": "002",
    "duration": "PT59M24S",
    "recordLabel": {
      "name": "Gortnahoo",
      "@id": "http://musicbrainz.org/label/699f13f1-c6d7-485f-a31e-92459c34657a",
      "@type": "MusicLabel"
    },
    "musicReleaseFormat": "http://schema.org/CDFormat",
    "name": "Just Piping",
    "@id": "http://musicbrainz.org/release/4c9190a2-6098-41f4-bbbf-7e9d41e3539e",
    "track": [
      {
        "trackNumber": "1.1",
        "name": "Frieze Britches",
        "@id": "http://musicbrainz.org/recording/b58d3c66-a22a-4659-a06b-b05ce16082d5",
        "duration": "PT02M44S",
        "@type": "MusicRecording"
      },
      {
        "trackNumber": "1.2",
        "duration": "PT04M33S",
        "name": "Colonel Frazier",
        "@id": "http://musicbrainz.org/recording/718f1532-45a2-4135-86c2-f5dd5c6b0be4",
        "@type": "MusicRecording"
      },
      {
        "@type": "MusicRecording",
        "duration": "PT04M42S",
        "@id": "http://musicbrainz.org/recording/a7359af1-d8e7-4433-b0a7-df88f0e9414d",
        "name": "Andy's & The Shaskeen",
        "trackNumber": "1.3"
      },
      {
        "@id": "http://musicbrainz.org/recording/415cbf95-edbf-4b9c-b4b6-f1a542e9fa73",
        "name": "Two Jigs",
        "duration": "PT03M15S",
        "@type": "MusicRecording",
        "trackNumber": "1.4"
      },
      {
        "@type": "MusicRecording",
        "@id": "http://musicbrainz.org/recording/6c6f1bd0-c4eb-47a7-9b59-c34ecb493053",
        "name": "McGreevy's 1 & 2 and the Master's Return",
        "duration": "PT04M15S",
        "trackNumber": "1.5"
      },
      {
        "trackNumber": "1.6",
        "@type": "MusicRecording",
        "@id": "http://musicbrainz.org/recording/4f58aab4-6155-4941-83fb-7fb60ce08220",
        "name": "Dear Irish Boy",
        "duration": "PT03M04S"
      },
      {
        "trackNumber": "1.7",
        "@type": "MusicRecording",
        "duration": "PT03M47S",
        "@id": "http://musicbrainz.org/recording/06be7dbf-6158-4f54-abe8-d3ca750f93df",
        "name": "The Inishcaultra Selection"
      },
      {
        "name": "Crehan's, Droney's & McGreevy's",
        "@id": "http://musicbrainz.org/recording/41bb730f-1aaf-4fea-9218-267e4f15c5bd",
        "duration": "PT03M20S",
        "@type": "MusicRecording",
        "trackNumber": "1.8"
      },
      {
        "trackNumber": "1.9",
        "duration": "PT04M40S",
        "name": "Garden of Daisies & The Job of Journeywork",
        "@id": "http://musicbrainz.org/recording/408ddba0-0dbb-46c8-830c-d45065319767",
        "@type": "MusicRecording"
      },
      {
        "trackNumber": "1.10",
        "@type": "MusicRecording",
        "@id": "http://musicbrainz.org/recording/c3141805-11fe-4667-8fbf-0bfd35d7d0b2",
        "name": "Sean Dwyer",
        "duration": "PT03M20S"
      },
      {
        "trackNumber": "1.11",
        "@id": "http://musicbrainz.org/recording/b8530e31-a002-493d-9b64-c9bb1f06d18c",
        "name": "Humours of Ballyloughlin",
        "duration": "PT02M17S",
        "@type": "MusicRecording"
      },
      {
        "duration": "PT02M22S",
        "@id": "http://musicbrainz.org/recording/0e951712-be5f-4b3d-9d4d-9b79605a041d",
        "name": "Bucks of Oranmore",
        "@type": "MusicRecording",
        "trackNumber": "1.12"
      },
      {
        "trackNumber": "1.13",
        "duration": "PT05M07S",
        "@id": "http://musicbrainz.org/recording/02a1e71d-7532-499e-9947-9a38ecc744ac",
        "name": "New House Selection",
        "@type": "MusicRecording"
      },
      {
        "@type": "MusicRecording",
        "duration": "PT02M52S",
        "name": "Blind Mary",
        "@id": "http://musicbrainz.org/recording/48dc4396-052d-4d73-beb8-8c3b0d66f511",
        "trackNumber": "1.14"
      },
      {
        "trackNumber": "1.15",
        "duration": "PT02M33S",
        "name": "Boy in the Boat & Pretty Girls of Mayo",
        "@id": "http://musicbrainz.org/recording/20f4e8c6-14e8-43a1-823e-8a39ebf25a21",
        "@type": "MusicRecording"
      },
      {
        "duration": "PT03M18S",
        "@id": "http://musicbrainz.org/recording/fa9f664d-915e-4502-aa1e-1d781c6008c3",
        "name": "The Commons Polkas",
        "@type": "MusicRecording",
        "trackNumber": "1.16"
      },
      {
        "trackNumber": "1.17",
        "duration": "PT03M15S",
        "@id": "http://musicbrainz.org/recording/ccb0454c-69a3-4be1-ab60-c31d5103c048",
        "name": "The Tempest & People's 1 & 2",
        "@type": "MusicRecording"
      }
    ],
    "sameAs": "https://rateyourmusic.com/release/album/michael_cooney_f2/just_piping.p/",
    "releaseOf": {
      "albumProductionType": "http://schema.org/StudioAlbum",
      "albumReleaseType": "http://schema.org/AlbumRelease",
      "byArtist": {
        "@type": [
          "Person",
          "MusicGroup"
        ],
        "@id": "http://musicbrainz.org/artist/b53568e7-9c3b-4186-9226-b5b1013f2780",
        "name": "Michael Cooney"
      },
      "creditedTo": "Michael Cooney",
      "name": "Just Piping",
      "@id": "http://musicbrainz.org/release-group/9939251d-839c-4a0c-bd0c-5ae224e7fcb9",
      "@type": "MusicAlbum"
    },
    "@context": [
      "https://schema.org/docs/jsonldcontext.json",
      "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/musicbrainz/jsonld/looping-approach/context.jsonld"
    ],
    "@type": "MusicRelease",
    "database": "https://musicbrainz.org/"
  }]

with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(data), indent=2))