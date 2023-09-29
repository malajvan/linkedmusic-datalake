from pyld import jsonld
import json

        
tested =      {
        "popularity_tunebooks": 5279,
        "tunes_name": "Cooley's",
        "recordings": [
            {
                "@id": "thesession:recordings/3536",
                "@type": "wd:Q3302947",
                "artist": "Accord\u00e9onistes Du Qu\u00e9bec",
                "recording": "Dans Tous Les Cantons",
                "track": 23
            },
            {
                "@id": "thesession:recordings/872",
                "@type": "wd:Q3302947",
                "artist": "Alan McCartney, Paul Bradley, Jason O'Rourke, Brendan O'Hare and Ray Gallen",
                "recording": "Traditional Irish Music From Belfast",
                "track": 9
            },
            {
                "@id": "thesession:recordings/5240",
                "@type": "wd:Q3302947",
                "artist": "Aly Bain and Mike Whellans",
                "recording": "Aly Bain and Mike Whellans",
                "track": 9
            },
            {
                "@id": "thesession:recordings/6081",
                "@type": "wd:Q3302947",
                "artist": "Alycia Putnam",
                "recording": "Wired for Sound",
                "track": 2
            },
            {
                "@id": "thesession:recordings/6642",
                "@type": "wd:Q3302947",
                "artist": "An Tara",
                "recording": "the space between",
                "track": 3
            },
            {
                "@id": "thesession:recordings/1671",
                "@type": "wd:Q3302947",
                "artist": "Annwn",
                "recording": "Anarchy And Rapture",
                "track": 5
            },
            {
                "@id": "thesession:recordings/2319",
                "@type": "wd:Q3302947",
                "artist": "Ar Leitheidi",
                "recording": "The Ulster Outcry",
                "track": 11
            },
            {
                "@id": "thesession:recordings/6819",
                "@type": "wd:Q3302947",
                "artist": "Augusta C\u00e9il\u00ed Band",
                "recording": "Volume 1",
                "track": 20
            },
            {
                "@id": "thesession:recordings/7520",
                "@type": "wd:Q3302947",
                "artist": "Bernie Geraghty & Monica Naughton",
                "recording": "Tongs By The Fire",
                "track": 5
            },
            {
                "@id": "thesession:recordings/594",
                "@type": "wd:Q3302947",
                "artist": "Blackbeers",
                "recording": "Drink The Night Away",
                "track": 16
            },
            {
                "@id": "thesession:recordings/5315",
                "@type": "wd:Q3302947",
                "artist": "Blackthorn (Canada)",
                "recording": "Market Town",
                "track": 8
            },
            {
                "@id": "thesession:recordings/2650",
                "@type": "wd:Q3302947",
                "artist": "Blackthorn Band",
                "recording": "Far From Home",
                "track": 3
            },
            {
                "@id": "thesession:recordings/3455",
                "@type": "wd:Q3302947",
                "artist": "Bobby Casey, Gabriel McKeon, Raymond Roland, Liam Farrell and John Roe",
                "recording": "Traditional Irish Music From Galway And Clare",
                "track": 6
            },
            {
                "@id": "thesession:recordings/6818",
                "@type": "wd:Q3302947",
                "artist": "Boots For Maggie",
                "recording": "Acushla",
                "track": 4
            },
            {
                "@id": "thesession:recordings/925",
                "@type": "wd:Q3302947",
                "artist": "Brian Mac Aodha",
                "recording": "Throw Away The Keys",
                "track": 12
            },
            {
                "@id": "thesession:recordings/995",
                "@type": "wd:Q3302947",
                "artist": "Caa A Dram",
                "recording": "One More...",
                "track": 1
            },
            {
                "@id": "thesession:recordings/6432",
                "@type": "wd:Q3302947",
                "artist": "Callanish",
                "recording": "Far From Home",
                "track": 15
            },
            {
                "@id": "thesession:recordings/553",
                "@type": "wd:Q3302947",
                "artist": "Caoilte O'Suilleabhain",
                "recording": "Before Leaving",
                "track": 9
            },
            {
                "@id": "thesession:recordings/2965",
                "@type": "wd:Q3302947",
                "artist": "Celtic Music Society (East Rochester HS)",
                "recording": "The Devils Of Dublin",
                "track": 5
            },
            {
                "@id": "thesession:recordings/4745",
                "@type": "wd:Q3302947",
                "artist": "Celtic Whirl",
                "recording": "Celtic Whirl/Le Tourbillon Celtique",
                "track": 4
            },
            {
                "@id": "thesession:recordings/5255",
                "@type": "wd:Q3302947",
                "artist": "Celtica",
                "recording": "Nice as Apple Pie",
                "track": 1
            },
            {
                "@id": "thesession:recordings/1227",
                "@type": "wd:Q3302947",
                "artist": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "recording": "Foinn Seisi\u00fan 1",
                "track": 5
            },
            {
                "@id": "thesession:recordings/1227",
                "@type": "wd:Q3302947",
                "artist": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "recording": "Foinn Seisi\u00fan 1",
                "track": 28
            },
            {
                "@id": "thesession:recordings/7789",
                "@type": "wd:Q3302947",
                "artist": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "recording": "Foinn Seisi\u00fan 4",
                "track": 31
            },
            {
                "@id": "thesession:recordings/7789",
                "@type": "wd:Q3302947",
                "artist": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "recording": "Foinn Seisi\u00fan 4",
                "track": 47
            },
            {
                "@id": "thesession:recordings/1888",
                "@type": "wd:Q3302947",
                "artist": "Chris Droney",
                "recording": "Down From Bell Harbour",
                "track": 4
            },
            {
                "@id": "thesession:recordings/1633",
                "@type": "wd:Q3302947",
                "artist": "Chris Droney",
                "recording": "Irish Dance Music",
                "track": 3
            },
            {
                "@id": "thesession:recordings/3557",
                "@type": "wd:Q3302947",
                "artist": "Clan Tampa",
                "recording": "Tampa Session Sets, Vol. 1",
                "track": 7
            },
            {
                "@id": "thesession:recordings/1705",
                "@type": "wd:Q3302947",
                "artist": "Cliff Moses",
                "recording": "The Curlews",
                "track": 9
            },
            {
                "@id": "thesession:recordings/6136",
                "@type": "wd:Q3302947",
                "artist": "Coffee Zombies",
                "recording": "Percolatin'",
                "track": 5
            },
            {
                "@id": "thesession:recordings/6053",
                "@type": "wd:Q3302947",
                "artist": "Colm Keane",
                "recording": "Tune Song Tune",
                "track": 7
            },
            {
                "@id": "thesession:recordings/2757",
                "@type": "wd:Q3302947",
                "artist": "Cormac Breatnach",
                "recording": "Musical Journey",
                "track": 11
            },
            {
                "@id": "thesession:recordings/5293",
                "@type": "wd:Q3302947",
                "artist": "Craig Duncan",
                "recording": "Irish Dance",
                "track": 3
            },
            {
                "@id": "thesession:recordings/5380",
                "@type": "wd:Q3302947",
                "artist": "Craig Duncan",
                "recording": "Irish Dance",
                "track": 3
            },
            {
                "@id": "thesession:recordings/7305",
                "@type": "wd:Q3302947",
                "artist": "Culann's Hounds",
                "recording": "One For The Road",
                "track": 10
            },
            {
                "@id": "thesession:recordings/6247",
                "@type": "wd:Q3302947",
                "artist": "Danette Eddy",
                "recording": "Motion Potion",
                "track": 4
            },
            {
                "@id": "thesession:recordings/5173",
                "@type": "wd:Q3302947",
                "artist": "Dannsair",
                "recording": "Gal\u00edcia",
                "track": 5
            },
            {
                "@id": "thesession:recordings/5841",
                "@type": "wd:Q3302947",
                "artist": "Dara Smith-MacDonald",
                "recording": "Connections",
                "track": 8
            },
            {
                "@id": "thesession:recordings/1139",
                "@type": "wd:Q3302947",
                "artist": "David Lindquist",
                "recording": "Step This Way",
                "track": 8
            },
            {
                "@id": "thesession:recordings/6408",
                "@type": "wd:Q3302947",
                "artist": "Deenagh C\u00e9il\u00ed Band",
                "recording": "Around the House",
                "track": 4
            },
            {
                "@id": "thesession:recordings/3964",
                "@type": "wd:Q3302947",
                "artist": "DinoTrad",
                "recording": "Seisiun Ceol Neachtains",
                "track": 1
            },
            {
                "@id": "thesession:recordings/7267",
                "@type": "wd:Q3302947",
                "artist": "Duilleoga",
                "recording": "Irish Bites",
                "track": 4
            },
            {
                "@id": "thesession:recordings/3464",
                "@type": "wd:Q3302947",
                "artist": "Dusty Banjos",
                "recording": "Live At The Crane",
                "track": 13
            },
            {
                "@id": "thesession:recordings/2403",
                "@type": "wd:Q3302947",
                "artist": "\u00c9amonn Coyne and Kris Drever",
                "recording": "Honk Toot Suite",
                "track": 8
            },
            {
                "@id": "thesession:recordings/5051",
                "@type": "wd:Q3302947",
                "artist": "Eddie Moloney",
                "recording": "Master Musician, Disc 2 of 2",
                "track": 12
            },
            {
                "@id": "thesession:recordings/477",
                "@type": "wd:Q3302947",
                "artist": "Eoin O'Neill",
                "recording": "In Session",
                "track": 9
            },
            {
                "@id": "thesession:recordings/2318",
                "@type": "wd:Q3302947",
                "artist": "Fianna",
                "recording": "Crame On",
                "track": 7
            },
            {
                "@id": "thesession:recordings/2867",
                "@type": "wd:Q3302947",
                "artist": "Fiddlers 3",
                "recording": "Volume 3: The Rhythm Chapter",
                "track": 5
            },
            {
                "@id": "thesession:recordings/3811",
                "@type": "wd:Q3302947",
                "artist": "Figgy Duff",
                "recording": "After The Tempest",
                "track": 4
            },
            {
                "@id": "thesession:recordings/1122",
                "@type": "wd:Q3302947",
                "artist": "Filska",
                "recording": "A Thousand Miles Away",
                "track": 1
            },
            {
                "@id": "thesession:recordings/2321",
                "@type": "wd:Q3302947",
                "artist": "Florie Brown",
                "recording": "Best Of Irish Fiddle",
                "track": 12
            },
            {
                "@id": "thesession:recordings/4723",
                "@type": "wd:Q3302947",
                "artist": "Folk Road",
                "recording": "Folk Road",
                "track": 2
            },
            {
                "@id": "thesession:recordings/1680",
                "@type": "wd:Q3302947",
                "artist": "Frank Ferrel",
                "recording": "Fiddledance",
                "track": 4
            },
            {
                "@id": "thesession:recordings/208",
                "@type": "wd:Q3302947",
                "artist": "Frankie Gavin and Paul Brock",
                "recording": "\u00d3m\u00f3s Do Joe Cooley",
                "track": 1
            },
            {
                "@id": "thesession:recordings/127",
                "@type": "wd:Q3302947",
                "artist": "Gaelic Storm",
                "recording": "Gaelic Storm",
                "track": 8
            },
            {
                "@id": "thesession:recordings/7360",
                "@type": "wd:Q3302947",
                "artist": "Geoff Purvis",
                "recording": "The Border Fiddler",
                "track": 3
            },
            {
                "@id": "thesession:recordings/7636",
                "@type": "wd:Q3302947",
                "artist": "Giacomo Sovrani",
                "recording": "Irish Tunes",
                "track": 1
            },
            {
                "@id": "thesession:recordings/2523",
                "@type": "wd:Q3302947",
                "artist": "Greanstalk",
                "recording": "Dratsville",
                "track": 8
            },
            {
                "@id": "thesession:recordings/6212",
                "@type": "wd:Q3302947",
                "artist": "Guilderoy Byrne",
                "recording": "Turning Away",
                "track": 9
            },
            {
                "@id": "thesession:recordings/6794",
                "@type": "wd:Q3302947",
                "artist": "Herv\u00e9 Cantal",
                "recording": "For the Sake of Old Decency",
                "track": 10
            },
            {
                "@id": "thesession:recordings/2307",
                "@type": "wd:Q3302947",
                "artist": "Howie MacDonald",
                "recording": "WhY2Keilidh",
                "track": 13
            },
            {
                "@id": "thesession:recordings/6975",
                "@type": "wd:Q3302947",
                "artist": "Irishields",
                "recording": "The Last Night In Doolin",
                "track": 3
            },
            {
                "@id": "thesession:recordings/3410",
                "@type": "wd:Q3302947",
                "artist": "Jean-Yves Le Pape",
                "recording": "The Uilleann Pipes Of Ireland",
                "track": 2
            },
            {
                "@id": "thesession:recordings/1664",
                "@type": "wd:Q3302947",
                "artist": "Jerry Holland",
                "recording": "Crystal Clear",
                "track": 3
            },
            {
                "@id": "thesession:recordings/6094",
                "@type": "wd:Q3302947",
                "artist": "Jimmy Power",
                "recording": "Go Home And Have Your Dinner",
                "track": 30
            },
            {
                "@id": "thesession:recordings/6859",
                "@type": "wd:Q3302947",
                "artist": "Jimmy Power and Tony Ledwith",
                "recording": "Irish Music from The Favourite",
                "track": 8
            },
            {
                "@id": "thesession:recordings/1778",
                "@type": "wd:Q3302947",
                "artist": "John Carty",
                "recording": "I Will If I Can",
                "track": 9
            },
            {
                "@id": "thesession:recordings/4186",
                "@type": "wd:Q3302947",
                "artist": "John Cronin And Daith\u00ed Kearney",
                "recording": "Midleton Rare",
                "track": 8
            },
            {
                "@id": "thesession:recordings/2694",
                "@type": "wd:Q3302947",
                "artist": "John G. Walsh",
                "recording": "The Galway Rambler",
                "track": 10
            },
            {
                "@id": "thesession:recordings/2232",
                "@type": "wd:Q3302947",
                "artist": "John Gannon",
                "recording": "Melodeon",
                "track": 1
            },
            {
                "@id": "thesession:recordings/7268",
                "@type": "wd:Q3302947",
                "artist": "John McCormick and Mary Vanorny",
                "recording": "In the Tap Room",
                "track": 19
            },
            {
                "@id": "thesession:recordings/2070",
                "@type": "wd:Q3302947",
                "artist": "John McGreevy And Seamus Cooley",
                "recording": "McGreevy And Cooley",
                "track": 15
            },
            {
                "@id": "thesession:recordings/4066",
                "@type": "wd:Q3302947",
                "artist": "John Weed And Stuart Mason",
                "recording": "Slow And Easy",
                "track": 4
            },
            {
                "@id": "thesession:recordings/1304",
                "@type": "wd:Q3302947",
                "artist": "Johnny Connolly",
                "recording": "Drioball na F\u00e1inleoige",
                "track": 4
            },
            {
                "@id": "thesession:recordings/7366",
                "@type": "wd:Q3302947",
                "artist": "Johnny Connolly with E. Kelly and P. Higgins",
                "recording": "Popular Irish C\u00e9il\u00ed Dances",
                "track": 4
            },
            {
                "@id": "thesession:recordings/2444",
                "@type": "wd:Q3302947",
                "artist": "Juniper",
                "recording": "Looking For A Rock",
                "track": 9
            },
            {
                "@id": "thesession:recordings/2037",
                "@type": "wd:Q3302947",
                "artist": "Katrien Delavier",
                "recording": "Harpes D'Irlande",
                "track": 10
            },
            {
                "@id": "thesession:recordings/1595",
                "@type": "wd:Q3302947",
                "artist": "Kennedy's Kitchen",
                "recording": "Kennedy's Kitchen",
                "track": 11
            },
            {
                "@id": "thesession:recordings/7718",
                "@type": "wd:Q3302947",
                "artist": "Kevin Keegan",
                "recording": "Irish Accordion",
                "track": 10
            },
            {
                "@id": "thesession:recordings/2844",
                "@type": "wd:Q3302947",
                "artist": "Kilkenny Road",
                "recording": "Kilkenny Road",
                "track": 2
            },
            {
                "@id": "thesession:recordings/4822",
                "@type": "wd:Q3302947",
                "artist": "King Chiaullee",
                "recording": "Reel:Ode",
                "track": 4
            },
            {
                "@id": "thesession:recordings/2155",
                "@type": "wd:Q3302947",
                "artist": "Knot Fibb'n",
                "recording": "Turning",
                "track": 5
            },
            {
                "@id": "thesession:recordings/4123",
                "@type": "wd:Q3302947",
                "artist": "Lamond Gillespie, Cormac Cannon And John Blake",
                "recording": "The Trip To Carrick",
                "track": 3
            },
            {
                "@id": "thesession:recordings/4961",
                "@type": "wd:Q3302947",
                "artist": "Leaping Lulu",
                "recording": "High Road, Low Road",
                "track": 4
            },
            {
                "@id": "thesession:recordings/5167",
                "@type": "wd:Q3302947",
                "artist": "Lothlorien",
                "recording": "Saqi",
                "track": 12
            },
            {
                "@id": "thesession:recordings/5564",
                "@type": "wd:Q3302947",
                "artist": "Maggie Sansone",
                "recording": "Dance Upon the Shore",
                "track": 4
            },
            {
                "@id": "thesession:recordings/7132",
                "@type": "wd:Q3302947",
                "artist": "Maidhc Dain\u00edn \u00d3 S\u00e9",
                "recording": "\u00d3 Chicago go Carrach\u00e1n",
                "track": 8
            },
            {
                "@id": "thesession:recordings/3186",
                "@type": "wd:Q3302947",
                "artist": "M\u00e1irt\u00edn O'Connor, Cathal Hayden, Seamie O'Dowd",
                "recording": "Crossroads",
                "track": 13
            },
            {
                "@id": "thesession:recordings/5756",
                "@type": "wd:Q3302947",
                "artist": "Mark  Prescott",
                "recording": "Step with Annette ~ Music for Old Style Step Dancing ~ Volume 1",
                "track": 3
            },
            {
                "@id": "thesession:recordings/5756",
                "@type": "wd:Q3302947",
                "artist": "Mark  Prescott",
                "recording": "Step with Annette ~ Music for Old Style Step Dancing ~ Volume 1",
                "track": 7
            },
            {
                "@id": "thesession:recordings/3421",
                "@type": "wd:Q3302947",
                "artist": "Martin Donohoe",
                "recording": "Tasty Touches CD 1",
                "track": 2
            },
            {
                "@id": "thesession:recordings/2467",
                "@type": "wd:Q3302947",
                "artist": "Matt Cunningham",
                "recording": "Dance Music Of Ireland, Volume 3",
                "track": 24
            },
            {
                "@id": "thesession:recordings/2546",
                "@type": "wd:Q3302947",
                "artist": "Matt Cunningham",
                "recording": "Dance Music Of Ireland, Volume 3 ~ CD Version",
                "track": 2
            },
            {
                "@id": "thesession:recordings/3073",
                "@type": "wd:Q3302947",
                "artist": "Matt Cunningham",
                "recording": "Memories Of Ireland",
                "track": 11
            },
            {
                "@id": "thesession:recordings/5639",
                "@type": "wd:Q3302947",
                "artist": "Mayo Yanachi",
                "recording": "Eat, Sleep, Fiddle",
                "track": 3
            },
            {
                "@id": "thesession:recordings/1163",
                "@type": "wd:Q3302947",
                "artist": "Michael Gorman",
                "recording": "The Sligo Champion (CD 1 of 2)",
                "track": 22
            },
            {
                "@id": "thesession:recordings/4191",
                "@type": "wd:Q3302947",
                "artist": "Michael Ryan",
                "recording": "Bees Wing",
                "track": 2
            },
            {
                "@id": "thesession:recordings/4415",
                "@type": "wd:Q3302947",
                "artist": "Michael Sexton C\u00e9il\u00ed Band",
                "recording": "Michael Sexton Ceili Band, Volume 2: Mad to Dance",
                "track": 19
            },
            {
                "@id": "thesession:recordings/5631",
                "@type": "wd:Q3302947",
                "artist": "Micheal Darby O Fatharta",
                "recording": "An Rithim R\u00e9idh",
                "track": 1
            },
            {
                "@id": "thesession:recordings/442",
                "@type": "wd:Q3302947",
                "artist": "Micheal Darby O Fatharta",
                "recording": "Bosca Bideach",
                "track": 2
            },
            {
                "@id": "thesession:recordings/4520",
                "@type": "wd:Q3302947",
                "artist": "Mithril",
                "recording": "Live in Concert",
                "track": 1
            },
            {
                "@id": "thesession:recordings/639",
                "@type": "wd:Q3302947",
                "artist": "Na Fili",
                "recording": "An Ghaoth Anair (The West Wind)",
                "track": 5
            },
            {
                "@id": "thesession:recordings/5893",
                "@type": "wd:Q3302947",
                "artist": "Noel Bermingham",
                "recording": "When The Tide Is Out",
                "track": 3
            },
            {
                "@id": "thesession:recordings/27",
                "@type": "wd:Q3302947",
                "artist": "Noel Hill And Tony Linnane",
                "recording": "Noel Hill And Tony Linnane",
                "track": 12
            },
            {
                "@id": "thesession:recordings/1386",
                "@type": "wd:Q3302947",
                "artist": "Oisin",
                "recording": "Bealoideas",
                "track": 10
            },
            {
                "@id": "thesession:recordings/7277",
                "@type": "wd:Q3302947",
                "artist": "P.J. Hernon, Domhnaill Hernon, S\u00e9amus Hernon and Eoin Hernon",
                "recording": "P.J. Hernon and Sons",
                "track": 15
            },
            {
                "@id": "thesession:recordings/7595",
                "@type": "wd:Q3302947",
                "artist": "Pat O'Connor and Brendan Hearty",
                "recording": "Glaise",
                "track": 4
            },
            {
                "@id": "thesession:recordings/1402",
                "@type": "wd:Q3302947",
                "artist": "Pendragon",
                "recording": "Artistic License",
                "track": 4
            },
            {
                "@id": "thesession:recordings/7539",
                "@type": "wd:Q3302947",
                "artist": "Peter O'Loughlin",
                "recording": "A Musical Life",
                "track": 12
            },
            {
                "@id": "thesession:recordings/7539",
                "@type": "wd:Q3302947",
                "artist": "Peter O'Loughlin",
                "recording": "A Musical Life",
                "track": 20
            },
            {
                "@id": "thesession:recordings/898",
                "@type": "wd:Q3302947",
                "artist": "Philippe Barnes",
                "recording": "An Feochan",
                "track": 6
            },
            {
                "@id": "thesession:recordings/7857",
                "@type": "wd:Q3302947",
                "artist": "PRISMA",
                "recording": "In the Streets of London",
                "track": 4
            },
            {
                "@id": "thesession:recordings/3279",
                "@type": "wd:Q3302947",
                "artist": "Queen's Gambit",
                "recording": "Fianchetto",
                "track": 5
            },
            {
                "@id": "thesession:recordings/4104",
                "@type": "wd:Q3302947",
                "artist": "Quentin Cooper, Eoin O'Neill, Eimear Howley",
                "recording": "The Fiddle Case",
                "track": 6
            },
            {
                "@id": "thesession:recordings/1562",
                "@type": "wd:Q3302947",
                "artist": "Rapalje",
                "recording": "Rakish Paddies",
                "track": 11
            },
            {
                "@id": "thesession:recordings/2766",
                "@type": "wd:Q3302947",
                "artist": "Rattle The Boards",
                "recording": "Rattle The Boards",
                "track": 6
            },
            {
                "@id": "thesession:recordings/4296",
                "@type": "wd:Q3302947",
                "artist": "Ray Gallen",
                "recording": "The Man of the House",
                "track": 14
            },
            {
                "@id": "thesession:recordings/2866",
                "@type": "wd:Q3302947",
                "artist": "Rick May And Gil Yslas",
                "recording": "Kids In A Candy Store",
                "track": 5
            },
            {
                "@id": "thesession:recordings/3306",
                "@type": "wd:Q3302947",
                "artist": "Robert Chalmers And Friends",
                "recording": "Sunday Night",
                "track": 1
            },
            {
                "@id": "thesession:recordings/2382",
                "@type": "wd:Q3302947",
                "artist": "Rud Eile",
                "recording": "Rud Eile",
                "track": 14
            },
            {
                "@id": "thesession:recordings/934",
                "@type": "wd:Q3302947",
                "artist": "Russell's House",
                "recording": "Russell's House",
                "track": 2
            },
            {
                "@id": "thesession:recordings/944",
                "@type": "wd:Q3302947",
                "artist": "Seamus Walshe",
                "recording": "Memories Of Galway",
                "track": 11
            },
            {
                "@id": "thesession:recordings/2922",
                "@type": "wd:Q3302947",
                "artist": "Sean Maguire",
                "recording": "A Man Apart",
                "track": 1
            },
            {
                "@id": "thesession:recordings/893",
                "@type": "wd:Q3302947",
                "artist": "Sean McGuire",
                "recording": "Music Of Ireland (Original Recording Digitally Remastered)",
                "track": 6
            },
            {
                "@id": "thesession:recordings/6904",
                "@type": "wd:Q3302947",
                "artist": "Se\u00e1n Ryan & Dan Coughlan",
                "recording": "Ryan & Coughlan, Vol. 1",
                "track": 11
            },
            {
                "@id": "thesession:recordings/6898",
                "@type": "wd:Q3302947",
                "artist": "Sean Ryan and Dan Coughlan",
                "recording": "Ryan & Coughlan, Vol 4",
                "track": 22
            },
            {
                "@id": "thesession:recordings/3801",
                "@type": "wd:Q3302947",
                "artist": "Sharon Corr",
                "recording": "Dream Of You",
                "track": 8
            },
            {
                "@id": "thesession:recordings/2152",
                "@type": "wd:Q3302947",
                "artist": "Shaskeen",
                "recording": "The Joys Of Life",
                "track": 8
            },
            {
                "@id": "thesession:recordings/4867",
                "@type": "wd:Q3302947",
                "artist": "Shift",
                "recording": "Shift",
                "track": 7
            },
            {
                "@id": "thesession:recordings/1887",
                "@type": "wd:Q3302947",
                "artist": "Spiral Seisi\u00fan",
                "recording": "Tripping Down The Stairs",
                "track": 1
            },
            {
                "@id": "thesession:recordings/3270",
                "@type": "wd:Q3302947",
                "artist": "Spriggan",
                "recording": "Mind The Gap",
                "track": 2
            },
            {
                "@id": "thesession:recordings/4740",
                "@type": "wd:Q3302947",
                "artist": "St. James's Gate",
                "recording": "St. James's Gate",
                "track": 10
            },
            {
                "@id": "thesession:recordings/3150",
                "@type": "wd:Q3302947",
                "artist": "Stanley And Grimm",
                "recording": "Stanley And Grimm, Another Round",
                "track": 12
            },
            {
                "@id": "thesession:recordings/6841",
                "@type": "wd:Q3302947",
                "artist": "Strings & Things",
                "recording": "Turbulence",
                "track": 2
            },
            {
                "@id": "thesession:recordings/7583",
                "@type": "wd:Q3302947",
                "artist": "Swallowtail",
                "recording": "Swallowtail",
                "track": 3
            },
            {
                "@id": "thesession:recordings/1828",
                "@type": "wd:Q3302947",
                "artist": "Temple House C\u00e9il\u00ed Band",
                "recording": "Music for Sets - Vol. 2",
                "track": 15
            },
            {
                "@id": "thesession:recordings/2366",
                "@type": "wd:Q3302947",
                "artist": "The Abbey C\u00e9il\u00ed Band",
                "recording": "Bruach An TSul\u00e1in",
                "track": 4
            },
            {
                "@id": "thesession:recordings/1825",
                "@type": "wd:Q3302947",
                "artist": "The Blacksmiths",
                "recording": "Merrily Kissed The Quaker",
                "track": 7
            },
            {
                "@id": "thesession:recordings/5",
                "@type": "wd:Q3302947",
                "artist": "The Bothy Band",
                "recording": "Live In Concert",
                "track": 5
            },
            {
                "@id": "thesession:recordings/3854",
                "@type": "wd:Q3302947",
                "artist": "The C\u00e9il\u00ed Bandits",
                "recording": "The Ceili Bandits",
                "track": 1
            },
            {
                "@id": "thesession:recordings/6606",
                "@type": "wd:Q3302947",
                "artist": "The Celtic Fiddlers and Ceilidh Singers",
                "recording": "Passage",
                "track": 1
            },
            {
                "@id": "thesession:recordings/1422",
                "@type": "wd:Q3302947",
                "artist": "The Coleman Country C\u00e9il\u00ed Band",
                "recording": "The Coleman Country C\u00e9il\u00ed Band",
                "track": 6
            },
            {
                "@id": "thesession:recordings/2601",
                "@type": "wd:Q3302947",
                "artist": "The Crickard Brothers",
                "recording": "Musiques Traditionnelles D'Irlande",
                "track": 9
            },
            {
                "@id": "thesession:recordings/1573",
                "@type": "wd:Q3302947",
                "artist": "The Culchies",
                "recording": "Bruscar B\u00e1n",
                "track": 13
            },
            {
                "@id": "thesession:recordings/1255",
                "@type": "wd:Q3302947",
                "artist": "The Dubliners",
                "recording": "Celebration CD 1",
                "track": 4
            },
            {
                "@id": "thesession:recordings/5355",
                "@type": "wd:Q3302947",
                "artist": "The Esker Riada C\u00e9il\u00ed Band",
                "recording": "Come West along the Road",
                "track": 4
            },
            {
                "@id": "thesession:recordings/5465",
                "@type": "wd:Q3302947",
                "artist": "The Flying Toads",
                "recording": "Warts 'n All",
                "track": 2
            },
            {
                "@id": "thesession:recordings/7179",
                "@type": "wd:Q3302947",
                "artist": "The Gallowglass C\u00e9il\u00ed Band",
                "recording": "Irish Dancing Time",
                "track": 9
            },
            {
                "@id": "thesession:recordings/3237",
                "@type": "wd:Q3302947",
                "artist": "The Irish Experience",
                "recording": "Green Energy",
                "track": 12
            },
            {
                "@id": "thesession:recordings/6876",
                "@type": "wd:Q3302947",
                "artist": "The JSD Band",
                "recording": "Country Of The Blind",
                "track": 2
            },
            {
                "@id": "thesession:recordings/2113",
                "@type": "wd:Q3302947",
                "artist": "The Lahawns with Andrew Mac Namara",
                "recording": "Live At Winkles",
                "track": 14
            },
            {
                "@id": "thesession:recordings/4030",
                "@type": "wd:Q3302947",
                "artist": "The Liverpool C\u00e9il\u00ed Band",
                "recording": "Champions Twice",
                "track": 4
            },
            {
                "@id": "thesession:recordings/4345",
                "@type": "wd:Q3302947",
                "artist": "The Ned Devines",
                "recording": "Live at Finnegan's Wake",
                "track": 3
            },
            {
                "@id": "thesession:recordings/429",
                "@type": "wd:Q3302947",
                "artist": "The Nettles",
                "recording": "The Nettles",
                "track": 2
            },
            {
                "@id": "thesession:recordings/5064",
                "@type": "wd:Q3302947",
                "artist": "The Shaskeen C\u00e9il\u00ed Band, Malachy Doris C\u00e9il\u00ed Band, The Pride of Erin C\u00e9il\u00ed Band",
                "recording": "La Vera Musica C\u00e9il\u00ed Irlandese",
                "track": 11
            },
            {
                "@id": "thesession:recordings/2147",
                "@type": "wd:Q3302947",
                "artist": "The Tulla C\u00e9il\u00ed Band",
                "recording": "40th Anniversary 1946 - 1986",
                "track": 9
            },
            {
                "@id": "thesession:recordings/894",
                "@type": "wd:Q3302947",
                "artist": "The Tulla C\u00e9il\u00ed Band",
                "recording": "A Celebration Of 50 Years",
                "track": 9
            },
            {
                "@id": "thesession:recordings/1425",
                "@type": "wd:Q3302947",
                "artist": "The Tulla C\u00e9il\u00ed Band",
                "recording": "Echoes Of Erin",
                "track": 7
            },
            {
                "@id": "thesession:recordings/5876",
                "@type": "wd:Q3302947",
                "artist": "Theresa O'Grady",
                "recording": "BANJO'ista",
                "track": 12
            },
            {
                "@id": "thesession:recordings/4274",
                "@type": "wd:Q3302947",
                "artist": "Threepenny Bit",
                "recording": "Something...",
                "track": 7
            },
            {
                "@id": "thesession:recordings/5579",
                "@type": "wd:Q3302947",
                "artist": "Tom Byrne and Tom McCaffrey",
                "recording": "Irish Music from Cleveland",
                "track": 17
            },
            {
                "@id": "thesession:recordings/7687",
                "@type": "wd:Q3302947",
                "artist": "Tom Doherty",
                "recording": "Dance Sean N\u00f3s",
                "track": 1
            },
            {
                "@id": "thesession:recordings/1210",
                "@type": "wd:Q3302947",
                "artist": "Tom Doherty",
                "recording": "Take The Bull By The Horns",
                "track": 11
            },
            {
                "@id": "thesession:recordings/325",
                "@type": "wd:Q3302947",
                "artist": "Tony MacMahon",
                "recording": "Traditional Irish Accordion",
                "track": 1
            },
            {
                "@id": "thesession:recordings/6778",
                "@type": "wd:Q3302947",
                "artist": "Toyota C\u00e9il\u00ed Band",
                "recording": "Gathering Cloud",
                "track": 8
            },
            {
                "@id": "thesession:recordings/5312",
                "@type": "wd:Q3302947",
                "artist": "Turlach Boylan",
                "recording": "Lift",
                "track": 11
            },
            {
                "@id": "thesession:recordings/4984",
                "@type": "wd:Q3302947",
                "artist": "Urban Celtic",
                "recording": "Urban Celtic",
                "track": 2
            },
            {
                "@id": "thesession:recordings/5906",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "\"Gort Tape\" CD 2 of 2",
                "track": 5
            },
            {
                "@id": "thesession:recordings/431",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Celtic Ceili",
                "track": 6
            },
            {
                "@id": "thesession:recordings/7167",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Celtic Jigs & Reels",
                "track": 2
            },
            {
                "@id": "thesession:recordings/5848",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Ceol na nOg",
                "track": 1
            },
            {
                "@id": "thesession:recordings/2607",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Ceol Tigh Neachtain - Music From Galway",
                "track": 7
            },
            {
                "@id": "thesession:recordings/5407",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Experience Ireland : Disc #1",
                "track": 15
            },
            {
                "@id": "thesession:recordings/4451",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Fishguard Folk - On a Sunday",
                "track": 14
            },
            {
                "@id": "thesession:recordings/1983",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "In The Footsteps Of Coleman",
                "track": 17
            },
            {
                "@id": "thesession:recordings/6874",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Irish Ceili - The Essential Collection (Irish Dance Music)",
                "track": 17
            },
            {
                "@id": "thesession:recordings/4404",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Irish Jigs & Reels",
                "track": 10
            },
            {
                "@id": "thesession:recordings/5359",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "It Was Great Altogether!  ~  CD 1 of 3",
                "track": 28
            },
            {
                "@id": "thesession:recordings/5343",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "It Was Mighty : CD #2",
                "track": 13
            },
            {
                "@id": "thesession:recordings/1032",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Music For The Sets Volume 3: Pay The Piper",
                "track": 12
            },
            {
                "@id": "thesession:recordings/4629",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Nights in Shanaglish",
                "track": 16
            },
            {
                "@id": "thesession:recordings/2516",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "Paddy And Bridget And Their Great Friends 2",
                "track": 1
            },
            {
                "@id": "thesession:recordings/3070",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "The Blackberry Blossom - Celtic Jigs & Reels",
                "track": 2
            },
            {
                "@id": "thesession:recordings/3070",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "The Blackberry Blossom - Celtic Jigs & Reels",
                "track": 11
            },
            {
                "@id": "thesession:recordings/2492",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "The Coleman Archive Volume 2: The Home Place",
                "track": 17
            },
            {
                "@id": "thesession:recordings/2492",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "The Coleman Archive Volume 2: The Home Place",
                "track": 19
            },
            {
                "@id": "thesession:recordings/1460",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "The Real Reels Of Ireland",
                "track": 17
            },
            {
                "@id": "thesession:recordings/4914",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "The Stockport Sea",
                "track": 1
            },
            {
                "@id": "thesession:recordings/5316",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "We're Irish Still",
                "track": 1
            },
            {
                "@id": "thesession:recordings/5316",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "We're Irish Still",
                "track": 4
            },
            {
                "@id": "thesession:recordings/5316",
                "@type": "wd:Q3302947",
                "artist": "Various Artists",
                "recording": "We're Irish Still",
                "track": 24
            },
            {
                "@id": "thesession:recordings/6444",
                "@type": "wd:Q3302947",
                "artist": "Vince Collins",
                "recording": "Over Home",
                "track": 11
            },
            {
                "@id": "thesession:recordings/3505",
                "@type": "wd:Q3302947",
                "artist": "Wendy MacIsaac",
                "recording": "The 'Reel' Thing",
                "track": 6
            },
            {
                "@id": "thesession:recordings/6430",
                "@type": "wd:Q3302947",
                "artist": "Wild Clover Band",
                "recording": "Behind The Blarney",
                "track": 2
            },
            {
                "@id": "thesession:recordings/1446",
                "@type": "wd:Q3302947",
                "artist": "William Sullivan",
                "recording": "Traditional Irish Music",
                "track": 33
            }
        ],
        "@id": "tunes:1",
        "@type": "wd:Q2188189",
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/thesession/jsonld/context.json",
        "database": "thesession:",
        "alias": "['Cooleys', 'Joe Cooley', \"Joe Cooley's\", \"Joe Cooley's Fancy\", 'Joe Cooleys', \"Luttrell's Pass\", 'Put The Cake In The Dresser', 'Put The Cake On The Dresser', 'Reaping The Rye', 'R\u00edl Na Tula\u00ed', 'Tulla, The']",
        "settings": [
            {
                "@id": "https://thesession.org/tunes/1#setting1",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2001-05-14T18:45:18",
                "username": "Jeremy"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting12342",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Eminor",
                "date": "2002-06-11T15:43:50",
                "username": "donnchad"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting12343",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Eminor",
                "date": "2008-06-15T13:53:38",
                "username": "middlefaster"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting20796",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2013-02-01T03:04:27",
                "username": "Edgar Bolton"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting20960",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2013-02-17T18:29:47",
                "username": "sebastian the m3g4p0p"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting21423",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Eminor",
                "date": "2013-04-15T13:30:56",
                "username": "Edgar Bolton"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting22061",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2013-08-03T07:16:42",
                "username": "Tate"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting23915",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2014-04-03T21:29:58",
                "username": "ceolachan"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting24552",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2014-07-24T14:10:21",
                "username": "eamonn barr"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting25140",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2014-11-13T01:59:23",
                "username": "JACKB"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting29823",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2017-02-12T22:50:50",
                "username": "litewave27"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting31475",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2017-12-11T10:35:07",
                "username": "Sergei Ejov"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting39518",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2020-11-10T09:40:05",
                "username": "GraefinZahl"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting39604",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2020-11-20T17:10:55",
                "username": "Anonymous_Piper"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting40038",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2021-01-03T18:07:01",
                "username": "Michael Eskin"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting41887",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2021-09-05T23:38:46",
                "username": "shanachie"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting44243",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2022-06-29T20:38:40",
                "username": "Blunty026"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting44659",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2022-08-27T19:04:59",
                "username": "Blunty026"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting45226",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Edorian",
                "date": "2022-10-31T22:19:36",
                "username": "Madeleine Townley"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting46013",
                "@type": "wd:Q113899068",
                "type": "https://thesession.org/tunes/search?type=reel",
                "meter": "4/4",
                "mode": "Ddorian",
                "date": "2023-01-29T13:31:02",
                "username": "PhilPontoise"
            }
        ]
    }
    

with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))