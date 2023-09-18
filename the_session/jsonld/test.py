from pyld import jsonld
import json

        
tested =  {       
        
        "popularity_tunebooks": 5279,
        "@id": "tunes:1",
        "@type": "wd:Q2188189",
        "P1476": "Cooley's",
        "database": "thesession:",
        "P4970": "['Cooleys', 'Joe Cooley', \"Joe Cooley's\", \"Joe Cooley's Fancy\", 'Joe Cooleys', \"Luttrell's Pass\", 'Put The Cake In The Dresser', 'Put The Cake On The Dresser', 'Reaping The Rye', 'R\u00edl Na Tula\u00ed', 'Tulla, The']",
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/the_session/jsonld/context.json",
        "P2550": [
            {
                "@id": "recordings:3536",
                "@type": "wd:Q3302947",
                "P175": "Accord\u00e9onistes Du Qu\u00e9bec",
                "P1476": "Dans Tous Les Cantons",
                "P2635": 23
            },
            {
                "@id": "recordings:872",
                "@type": "wd:Q3302947",
                "P175": "Alan McCartney, Paul Bradley, Jason O'Rourke, Brendan O'Hare and Ray Gallen",
                "P1476": "Traditional Irish Music From Belfast",
                "P2635": 9
            },
            {
                "@id": "recordings:5240",
                "@type": "wd:Q3302947",
                "P175": "Aly Bain and Mike Whellans",
                "P1476": "Aly Bain and Mike Whellans",
                "P2635": 9
            },
            {
                "@id": "recordings:6081",
                "@type": "wd:Q3302947",
                "P175": "Alycia Putnam",
                "P1476": "Wired for Sound",
                "P2635": 2
            },
            {
                "@id": "recordings:6642",
                "@type": "wd:Q3302947",
                "P175": "An Tara",
                "P1476": "the space between",
                "P2635": 3
            },
            {
                "@id": "recordings:1671",
                "@type": "wd:Q3302947",
                "P175": "Annwn",
                "P1476": "Anarchy And Rapture",
                "P2635": 5
            },
            {
                "@id": "recordings:2319",
                "@type": "wd:Q3302947",
                "P175": "Ar Leitheidi",
                "P1476": "The Ulster Outcry",
                "P2635": 11
            },
            {
                "@id": "recordings:6819",
                "@type": "wd:Q3302947",
                "P175": "Augusta C\u00e9il\u00ed Band",
                "P1476": "Volume 1",
                "P2635": 20
            },
            {
                "@id": "recordings:7520",
                "@type": "wd:Q3302947",
                "P175": "Bernie Geraghty & Monica Naughton",
                "P1476": "Tongs By The Fire",
                "P2635": 5
            },
            {
                "@id": "recordings:594",
                "@type": "wd:Q3302947",
                "P175": "Blackbeers",
                "P1476": "Drink The Night Away",
                "P2635": 16
            },
            {
                "@id": "recordings:5315",
                "@type": "wd:Q3302947",
                "P175": "Blackthorn (Canada)",
                "P1476": "Market Town",
                "P2635": 8
            },
            {
                "@id": "recordings:2650",
                "@type": "wd:Q3302947",
                "P175": "Blackthorn Band",
                "P1476": "Far From Home",
                "P2635": 3
            },
            {
                "@id": "recordings:3455",
                "@type": "wd:Q3302947",
                "P175": "Bobby Casey, Gabriel McKeon, Raymond Roland, Liam Farrell and John Roe",
                "P1476": "Traditional Irish Music From Galway And Clare",
                "P2635": 6
            },
            {
                "@id": "recordings:6818",
                "@type": "wd:Q3302947",
                "P175": "Boots For Maggie",
                "P1476": "Acushla",
                "P2635": 4
            },
            {
                "@id": "recordings:925",
                "@type": "wd:Q3302947",
                "P175": "Brian Mac Aodha",
                "P1476": "Throw Away The Keys",
                "P2635": 12
            },
            {
                "@id": "recordings:995",
                "@type": "wd:Q3302947",
                "P175": "Caa A Dram",
                "P1476": "One More...",
                "P2635": 1
            },
            {
                "@id": "recordings:6432",
                "@type": "wd:Q3302947",
                "P175": "Callanish",
                "P1476": "Far From Home",
                "P2635": 15
            },
            {
                "@id": "recordings:553",
                "@type": "wd:Q3302947",
                "P175": "Caoilte O'Suilleabhain",
                "P1476": "Before Leaving",
                "P2635": 9
            },
            {
                "@id": "recordings:2965",
                "@type": "wd:Q3302947",
                "P175": "Celtic Music Society (East Rochester HS)",
                "P1476": "The Devils Of Dublin",
                "P2635": 5
            },
            {
                "@id": "recordings:4745",
                "@type": "wd:Q3302947",
                "P175": "Celtic Whirl",
                "P1476": "Celtic Whirl/Le Tourbillon Celtique",
                "P2635": 4
            },
            {
                "@id": "recordings:5255",
                "@type": "wd:Q3302947",
                "P175": "Celtica",
                "P1476": "Nice as Apple Pie",
                "P2635": 1
            },
            {
                "@id": "recordings:1227",
                "@type": "wd:Q3302947",
                "P175": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "P1476": "Foinn Seisi\u00fan 1",
                "P2635": 5
            },
            {
                "@id": "recordings:1227",
                "@type": "wd:Q3302947",
                "P175": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "P1476": "Foinn Seisi\u00fan 1",
                "P2635": 28
            },
            {
                "@id": "recordings:7789",
                "@type": "wd:Q3302947",
                "P175": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "P1476": "Foinn Seisi\u00fan 4",
                "P2635": 31
            },
            {
                "@id": "recordings:7789",
                "@type": "wd:Q3302947",
                "P175": "Ceolt\u00f3ir\u00ed Cult\u00farlainne",
                "P1476": "Foinn Seisi\u00fan 4",
                "P2635": 47
            },
            {
                "@id": "recordings:1888",
                "@type": "wd:Q3302947",
                "P175": "Chris Droney",
                "P1476": "Down From Bell Harbour",
                "P2635": 4
            },
            {
                "@id": "recordings:1633",
                "@type": "wd:Q3302947",
                "P175": "Chris Droney",
                "P1476": "Irish Dance Music",
                "P2635": 3
            },
            {
                "@id": "recordings:3557",
                "@type": "wd:Q3302947",
                "P175": "Clan Tampa",
                "P1476": "Tampa Session Sets, Vol. 1",
                "P2635": 7
            },
            {
                "@id": "recordings:1705",
                "@type": "wd:Q3302947",
                "P175": "Cliff Moses",
                "P1476": "The Curlews",
                "P2635": 9
            },
            {
                "@id": "recordings:6136",
                "@type": "wd:Q3302947",
                "P175": "Coffee Zombies",
                "P1476": "Percolatin'",
                "P2635": 5
            },
            {
                "@id": "recordings:6053",
                "@type": "wd:Q3302947",
                "P175": "Colm Keane",
                "P1476": "Tune Song Tune",
                "P2635": 7
            },
            {
                "@id": "recordings:2757",
                "@type": "wd:Q3302947",
                "P175": "Cormac Breatnach",
                "P1476": "Musical Journey",
                "P2635": 11
            },
            {
                "@id": "recordings:5293",
                "@type": "wd:Q3302947",
                "P175": "Craig Duncan",
                "P1476": "Irish Dance",
                "P2635": 3
            },
            {
                "@id": "recordings:5380",
                "@type": "wd:Q3302947",
                "P175": "Craig Duncan",
                "P1476": "Irish Dance",
                "P2635": 3
            },
            {
                "@id": "recordings:7305",
                "@type": "wd:Q3302947",
                "P175": "Culann's Hounds",
                "P1476": "One For The Road",
                "P2635": 10
            },
            {
                "@id": "recordings:6247",
                "@type": "wd:Q3302947",
                "P175": "Danette Eddy",
                "P1476": "Motion Potion",
                "P2635": 4
            },
            {
                "@id": "recordings:5173",
                "@type": "wd:Q3302947",
                "P175": "Dannsair",
                "P1476": "Gal\u00edcia",
                "P2635": 5
            },
            {
                "@id": "recordings:5841",
                "@type": "wd:Q3302947",
                "P175": "Dara Smith-MacDonald",
                "P1476": "Connections",
                "P2635": 8
            },
            {
                "@id": "recordings:1139",
                "@type": "wd:Q3302947",
                "P175": "David Lindquist",
                "P1476": "Step This Way",
                "P2635": 8
            },
            {
                "@id": "recordings:6408",
                "@type": "wd:Q3302947",
                "P175": "Deenagh C\u00e9il\u00ed Band",
                "P1476": "Around the House",
                "P2635": 4
            },
            {
                "@id": "recordings:3964",
                "@type": "wd:Q3302947",
                "P175": "DinoTrad",
                "P1476": "Seisiun Ceol Neachtains",
                "P2635": 1
            },
            {
                "@id": "recordings:7267",
                "@type": "wd:Q3302947",
                "P175": "Duilleoga",
                "P1476": "Irish Bites",
                "P2635": 4
            },
            {
                "@id": "recordings:3464",
                "@type": "wd:Q3302947",
                "P175": "Dusty Banjos",
                "P1476": "Live At The Crane",
                "P2635": 13
            },
            {
                "@id": "recordings:2403",
                "@type": "wd:Q3302947",
                "P175": "\u00c9amonn Coyne and Kris Drever",
                "P1476": "Honk Toot Suite",
                "P2635": 8
            },
            {
                "@id": "recordings:5051",
                "@type": "wd:Q3302947",
                "P175": "Eddie Moloney",
                "P1476": "Master Musician, Disc 2 of 2",
                "P2635": 12
            },
            {
                "@id": "recordings:477",
                "@type": "wd:Q3302947",
                "P175": "Eoin O'Neill",
                "P1476": "In Session",
                "P2635": 9
            },
            {
                "@id": "recordings:2318",
                "@type": "wd:Q3302947",
                "P175": "Fianna",
                "P1476": "Crame On",
                "P2635": 7
            },
            {
                "@id": "recordings:2867",
                "@type": "wd:Q3302947",
                "P175": "Fiddlers 3",
                "P1476": "Volume 3: The Rhythm Chapter",
                "P2635": 5
            },
            {
                "@id": "recordings:3811",
                "@type": "wd:Q3302947",
                "P175": "Figgy Duff",
                "P1476": "After The Tempest",
                "P2635": 4
            },
            {
                "@id": "recordings:1122",
                "@type": "wd:Q3302947",
                "P175": "Filska",
                "P1476": "A Thousand Miles Away",
                "P2635": 1
            },
            {
                "@id": "recordings:2321",
                "@type": "wd:Q3302947",
                "P175": "Florie Brown",
                "P1476": "Best Of Irish Fiddle",
                "P2635": 12
            },
            {
                "@id": "recordings:4723",
                "@type": "wd:Q3302947",
                "P175": "Folk Road",
                "P1476": "Folk Road",
                "P2635": 2
            },
            {
                "@id": "recordings:1680",
                "@type": "wd:Q3302947",
                "P175": "Frank Ferrel",
                "P1476": "Fiddledance",
                "P2635": 4
            },
            {
                "@id": "recordings:208",
                "@type": "wd:Q3302947",
                "P175": "Frankie Gavin and Paul Brock",
                "P1476": "\u00d3m\u00f3s Do Joe Cooley",
                "P2635": 1
            },
            {
                "@id": "recordings:127",
                "@type": "wd:Q3302947",
                "P175": "Gaelic Storm",
                "P1476": "Gaelic Storm",
                "P2635": 8
            },
            {
                "@id": "recordings:7360",
                "@type": "wd:Q3302947",
                "P175": "Geoff Purvis",
                "P1476": "The Border Fiddler",
                "P2635": 3
            },
            {
                "@id": "recordings:7636",
                "@type": "wd:Q3302947",
                "P175": "Giacomo Sovrani",
                "P1476": "Irish Tunes",
                "P2635": 1
            },
            {
                "@id": "recordings:2523",
                "@type": "wd:Q3302947",
                "P175": "Greanstalk",
                "P1476": "Dratsville",
                "P2635": 8
            },
            {
                "@id": "recordings:6212",
                "@type": "wd:Q3302947",
                "P175": "Guilderoy Byrne",
                "P1476": "Turning Away",
                "P2635": 9
            },
            {
                "@id": "recordings:6794",
                "@type": "wd:Q3302947",
                "P175": "Herv\u00e9 Cantal",
                "P1476": "For the Sake of Old Decency",
                "P2635": 10
            },
            {
                "@id": "recordings:2307",
                "@type": "wd:Q3302947",
                "P175": "Howie MacDonald",
                "P1476": "WhY2Keilidh",
                "P2635": 13
            },
            {
                "@id": "recordings:6975",
                "@type": "wd:Q3302947",
                "P175": "Irishields",
                "P1476": "The Last Night In Doolin",
                "P2635": 3
            },
            {
                "@id": "recordings:3410",
                "@type": "wd:Q3302947",
                "P175": "Jean-Yves Le Pape",
                "P1476": "The Uilleann Pipes Of Ireland",
                "P2635": 2
            },
            {
                "@id": "recordings:1664",
                "@type": "wd:Q3302947",
                "P175": "Jerry Holland",
                "P1476": "Crystal Clear",
                "P2635": 3
            },
            {
                "@id": "recordings:6094",
                "@type": "wd:Q3302947",
                "P175": "Jimmy Power",
                "P1476": "Go Home And Have Your Dinner",
                "P2635": 30
            },
            {
                "@id": "recordings:6859",
                "@type": "wd:Q3302947",
                "P175": "Jimmy Power and Tony Ledwith",
                "P1476": "Irish Music from The Favourite",
                "P2635": 8
            },
            {
                "@id": "recordings:1778",
                "@type": "wd:Q3302947",
                "P175": "John Carty",
                "P1476": "I Will If I Can",
                "P2635": 9
            },
            {
                "@id": "recordings:4186",
                "@type": "wd:Q3302947",
                "P175": "John Cronin And Daith\u00ed Kearney",
                "P1476": "Midleton Rare",
                "P2635": 8
            },
            {
                "@id": "recordings:2694",
                "@type": "wd:Q3302947",
                "P175": "John G. Walsh",
                "P1476": "The Galway Rambler",
                "P2635": 10
            },
            {
                "@id": "recordings:2232",
                "@type": "wd:Q3302947",
                "P175": "John Gannon",
                "P1476": "Melodeon",
                "P2635": 1
            },
            {
                "@id": "recordings:7268",
                "@type": "wd:Q3302947",
                "P175": "John McCormick and Mary Vanorny",
                "P1476": "In the Tap Room",
                "P2635": 19
            },
            {
                "@id": "recordings:2070",
                "@type": "wd:Q3302947",
                "P175": "John McGreevy And Seamus Cooley",
                "P1476": "McGreevy And Cooley",
                "P2635": 15
            },
            {
                "@id": "recordings:4066",
                "@type": "wd:Q3302947",
                "P175": "John Weed And Stuart Mason",
                "P1476": "Slow And Easy",
                "P2635": 4
            },
            {
                "@id": "recordings:1304",
                "@type": "wd:Q3302947",
                "P175": "Johnny Connolly",
                "P1476": "Drioball na F\u00e1inleoige",
                "P2635": 4
            },
            {
                "@id": "recordings:7366",
                "@type": "wd:Q3302947",
                "P175": "Johnny Connolly with E. Kelly and P. Higgins",
                "P1476": "Popular Irish C\u00e9il\u00ed Dances",
                "P2635": 4
            },
            {
                "@id": "recordings:2444",
                "@type": "wd:Q3302947",
                "P175": "Juniper",
                "P1476": "Looking For A Rock",
                "P2635": 9
            },
            {
                "@id": "recordings:2037",
                "@type": "wd:Q3302947",
                "P175": "Katrien Delavier",
                "P1476": "Harpes D'Irlande",
                "P2635": 10
            },
            {
                "@id": "recordings:1595",
                "@type": "wd:Q3302947",
                "P175": "Kennedy's Kitchen",
                "P1476": "Kennedy's Kitchen",
                "P2635": 11
            },
            {
                "@id": "recordings:7718",
                "@type": "wd:Q3302947",
                "P175": "Kevin Keegan",
                "P1476": "Irish Accordion",
                "P2635": 10
            },
            {
                "@id": "recordings:2844",
                "@type": "wd:Q3302947",
                "P175": "Kilkenny Road",
                "P1476": "Kilkenny Road",
                "P2635": 2
            },
            {
                "@id": "recordings:4822",
                "@type": "wd:Q3302947",
                "P175": "King Chiaullee",
                "P1476": "Reel:Ode",
                "P2635": 4
            },
            {
                "@id": "recordings:2155",
                "@type": "wd:Q3302947",
                "P175": "Knot Fibb'n",
                "P1476": "Turning",
                "P2635": 5
            },
            {
                "@id": "recordings:4123",
                "@type": "wd:Q3302947",
                "P175": "Lamond Gillespie, Cormac Cannon And John Blake",
                "P1476": "The Trip To Carrick",
                "P2635": 3
            },
            {
                "@id": "recordings:4961",
                "@type": "wd:Q3302947",
                "P175": "Leaping Lulu",
                "P1476": "High Road, Low Road",
                "P2635": 4
            },
            {
                "@id": "recordings:5167",
                "@type": "wd:Q3302947",
                "P175": "Lothlorien",
                "P1476": "Saqi",
                "P2635": 12
            },
            {
                "@id": "recordings:5564",
                "@type": "wd:Q3302947",
                "P175": "Maggie Sansone",
                "P1476": "Dance Upon the Shore",
                "P2635": 4
            },
            {
                "@id": "recordings:7132",
                "@type": "wd:Q3302947",
                "P175": "Maidhc Dain\u00edn \u00d3 S\u00e9",
                "P1476": "\u00d3 Chicago go Carrach\u00e1n",
                "P2635": 8
            },
            {
                "@id": "recordings:3186",
                "@type": "wd:Q3302947",
                "P175": "M\u00e1irt\u00edn O'Connor, Cathal Hayden, Seamie O'Dowd",
                "P1476": "Crossroads",
                "P2635": 13
            },
            {
                "@id": "recordings:5756",
                "@type": "wd:Q3302947",
                "P175": "Mark  Prescott",
                "P1476": "Step with Annette ~ Music for Old Style Step Dancing ~ Volume 1",
                "P2635": 3
            },
            {
                "@id": "recordings:5756",
                "@type": "wd:Q3302947",
                "P175": "Mark  Prescott",
                "P1476": "Step with Annette ~ Music for Old Style Step Dancing ~ Volume 1",
                "P2635": 7
            },
            {
                "@id": "recordings:3421",
                "@type": "wd:Q3302947",
                "P175": "Martin Donohoe",
                "P1476": "Tasty Touches CD 1",
                "P2635": 2
            },
            {
                "@id": "recordings:2467",
                "@type": "wd:Q3302947",
                "P175": "Matt Cunningham",
                "P1476": "Dance Music Of Ireland, Volume 3",
                "P2635": 24
            },
            {
                "@id": "recordings:2546",
                "@type": "wd:Q3302947",
                "P175": "Matt Cunningham",
                "P1476": "Dance Music Of Ireland, Volume 3 ~ CD Version",
                "P2635": 2
            },
            {
                "@id": "recordings:3073",
                "@type": "wd:Q3302947",
                "P175": "Matt Cunningham",
                "P1476": "Memories Of Ireland",
                "P2635": 11
            },
            {
                "@id": "recordings:5639",
                "@type": "wd:Q3302947",
                "P175": "Mayo Yanachi",
                "P1476": "Eat, Sleep, Fiddle",
                "P2635": 3
            },
            {
                "@id": "recordings:1163",
                "@type": "wd:Q3302947",
                "P175": "Michael Gorman",
                "P1476": "The Sligo Champion (CD 1 of 2)",
                "P2635": 22
            },
            {
                "@id": "recordings:4191",
                "@type": "wd:Q3302947",
                "P175": "Michael Ryan",
                "P1476": "Bees Wing",
                "P2635": 2
            },
            {
                "@id": "recordings:4415",
                "@type": "wd:Q3302947",
                "P175": "Michael Sexton C\u00e9il\u00ed Band",
                "P1476": "Michael Sexton Ceili Band, Volume 2: Mad to Dance",
                "P2635": 19
            },
            {
                "@id": "recordings:5631",
                "@type": "wd:Q3302947",
                "P175": "Micheal Darby O Fatharta",
                "P1476": "An Rithim R\u00e9idh",
                "P2635": 1
            },
            {
                "@id": "recordings:442",
                "@type": "wd:Q3302947",
                "P175": "Micheal Darby O Fatharta",
                "P1476": "Bosca Bideach",
                "P2635": 2
            },
            {
                "@id": "recordings:4520",
                "@type": "wd:Q3302947",
                "P175": "Mithril",
                "P1476": "Live in Concert",
                "P2635": 1
            },
            {
                "@id": "recordings:639",
                "@type": "wd:Q3302947",
                "P175": "Na Fili",
                "P1476": "An Ghaoth Anair (The West Wind)",
                "P2635": 5
            },
            {
                "@id": "recordings:5893",
                "@type": "wd:Q3302947",
                "P175": "Noel Bermingham",
                "P1476": "When The Tide Is Out",
                "P2635": 3
            },
            {
                "@id": "recordings:27",
                "@type": "wd:Q3302947",
                "P175": "Noel Hill And Tony Linnane",
                "P1476": "Noel Hill And Tony Linnane",
                "P2635": 12
            },
            {
                "@id": "recordings:1386",
                "@type": "wd:Q3302947",
                "P175": "Oisin",
                "P1476": "Bealoideas",
                "P2635": 10
            },
            {
                "@id": "recordings:7277",
                "@type": "wd:Q3302947",
                "P175": "P.J. Hernon, Domhnaill Hernon, S\u00e9amus Hernon and Eoin Hernon",
                "P1476": "P.J. Hernon and Sons",
                "P2635": 15
            },
            {
                "@id": "recordings:7595",
                "@type": "wd:Q3302947",
                "P175": "Pat O'Connor and Brendan Hearty",
                "P1476": "Glaise",
                "P2635": 4
            },
            {
                "@id": "recordings:1402",
                "@type": "wd:Q3302947",
                "P175": "Pendragon",
                "P1476": "Artistic License",
                "P2635": 4
            },
            {
                "@id": "recordings:7539",
                "@type": "wd:Q3302947",
                "P175": "Peter O'Loughlin",
                "P1476": "A Musical Life",
                "P2635": 12
            },
            {
                "@id": "recordings:7539",
                "@type": "wd:Q3302947",
                "P175": "Peter O'Loughlin",
                "P1476": "A Musical Life",
                "P2635": 20
            },
            {
                "@id": "recordings:898",
                "@type": "wd:Q3302947",
                "P175": "Philippe Barnes",
                "P1476": "An Feochan",
                "P2635": 6
            },
            {
                "@id": "recordings:7857",
                "@type": "wd:Q3302947",
                "P175": "PRISMA",
                "P1476": "In the Streets of London",
                "P2635": 4
            },
            {
                "@id": "recordings:3279",
                "@type": "wd:Q3302947",
                "P175": "Queen's Gambit",
                "P1476": "Fianchetto",
                "P2635": 5
            },
            {
                "@id": "recordings:4104",
                "@type": "wd:Q3302947",
                "P175": "Quentin Cooper, Eoin O'Neill, Eimear Howley",
                "P1476": "The Fiddle Case",
                "P2635": 6
            },
            {
                "@id": "recordings:1562",
                "@type": "wd:Q3302947",
                "P175": "Rapalje",
                "P1476": "Rakish Paddies",
                "P2635": 11
            },
            {
                "@id": "recordings:2766",
                "@type": "wd:Q3302947",
                "P175": "Rattle The Boards",
                "P1476": "Rattle The Boards",
                "P2635": 6
            },
            {
                "@id": "recordings:4296",
                "@type": "wd:Q3302947",
                "P175": "Ray Gallen",
                "P1476": "The Man of the House",
                "P2635": 14
            },
            {
                "@id": "recordings:2866",
                "@type": "wd:Q3302947",
                "P175": "Rick May And Gil Yslas",
                "P1476": "Kids In A Candy Store",
                "P2635": 5
            },
            {
                "@id": "recordings:3306",
                "@type": "wd:Q3302947",
                "P175": "Robert Chalmers And Friends",
                "P1476": "Sunday Night",
                "P2635": 1
            },
            {
                "@id": "recordings:2382",
                "@type": "wd:Q3302947",
                "P175": "Rud Eile",
                "P1476": "Rud Eile",
                "P2635": 14
            },
            {
                "@id": "recordings:934",
                "@type": "wd:Q3302947",
                "P175": "Russell's House",
                "P1476": "Russell's House",
                "P2635": 2
            },
            {
                "@id": "recordings:944",
                "@type": "wd:Q3302947",
                "P175": "Seamus Walshe",
                "P1476": "Memories Of Galway",
                "P2635": 11
            },
            {
                "@id": "recordings:2922",
                "@type": "wd:Q3302947",
                "P175": "Sean Maguire",
                "P1476": "A Man Apart",
                "P2635": 1
            },
            {
                "@id": "recordings:893",
                "@type": "wd:Q3302947",
                "P175": "Sean McGuire",
                "P1476": "Music Of Ireland (Original Recording Digitally Remastered)",
                "P2635": 6
            },
            {
                "@id": "recordings:6904",
                "@type": "wd:Q3302947",
                "P175": "Se\u00e1n Ryan & Dan Coughlan",
                "P1476": "Ryan & Coughlan, Vol. 1",
                "P2635": 11
            },
            {
                "@id": "recordings:6898",
                "@type": "wd:Q3302947",
                "P175": "Sean Ryan and Dan Coughlan",
                "P1476": "Ryan & Coughlan, Vol 4",
                "P2635": 22
            },
            {
                "@id": "recordings:3801",
                "@type": "wd:Q3302947",
                "P175": "Sharon Corr",
                "P1476": "Dream Of You",
                "P2635": 8
            },
            {
                "@id": "recordings:2152",
                "@type": "wd:Q3302947",
                "P175": "Shaskeen",
                "P1476": "The Joys Of Life",
                "P2635": 8
            },
            {
                "@id": "recordings:4867",
                "@type": "wd:Q3302947",
                "P175": "Shift",
                "P1476": "Shift",
                "P2635": 7
            },
            {
                "@id": "recordings:1887",
                "@type": "wd:Q3302947",
                "P175": "Spiral Seisi\u00fan",
                "P1476": "Tripping Down The Stairs",
                "P2635": 1
            },
            {
                "@id": "recordings:3270",
                "@type": "wd:Q3302947",
                "P175": "Spriggan",
                "P1476": "Mind The Gap",
                "P2635": 2
            },
            {
                "@id": "recordings:4740",
                "@type": "wd:Q3302947",
                "P175": "St. James's Gate",
                "P1476": "St. James's Gate",
                "P2635": 10
            },
            {
                "@id": "recordings:3150",
                "@type": "wd:Q3302947",
                "P175": "Stanley And Grimm",
                "P1476": "Stanley And Grimm, Another Round",
                "P2635": 12
            },
            {
                "@id": "recordings:6841",
                "@type": "wd:Q3302947",
                "P175": "Strings & Things",
                "P1476": "Turbulence",
                "P2635": 2
            },
            {
                "@id": "recordings:7583",
                "@type": "wd:Q3302947",
                "P175": "Swallowtail",
                "P1476": "Swallowtail",
                "P2635": 3
            },
            {
                "@id": "recordings:1828",
                "@type": "wd:Q3302947",
                "P175": "Temple House C\u00e9il\u00ed Band",
                "P1476": "Music for Sets - Vol. 2",
                "P2635": 15
            },
            {
                "@id": "recordings:2366",
                "@type": "wd:Q3302947",
                "P175": "The Abbey C\u00e9il\u00ed Band",
                "P1476": "Bruach An TSul\u00e1in",
                "P2635": 4
            },
            {
                "@id": "recordings:1825",
                "@type": "wd:Q3302947",
                "P175": "The Blacksmiths",
                "P1476": "Merrily Kissed The Quaker",
                "P2635": 7
            },
            {
                "@id": "recordings:5",
                "@type": "wd:Q3302947",
                "P175": "The Bothy Band",
                "P1476": "Live In Concert",
                "P2635": 5
            },
            {
                "@id": "recordings:3854",
                "@type": "wd:Q3302947",
                "P175": "The C\u00e9il\u00ed Bandits",
                "P1476": "The Ceili Bandits",
                "P2635": 1
            },
            {
                "@id": "recordings:6606",
                "@type": "wd:Q3302947",
                "P175": "The Celtic Fiddlers and Ceilidh Singers",
                "P1476": "Passage",
                "P2635": 1
            },
            {
                "@id": "recordings:1422",
                "@type": "wd:Q3302947",
                "P175": "The Coleman Country C\u00e9il\u00ed Band",
                "P1476": "The Coleman Country C\u00e9il\u00ed Band",
                "P2635": 6
            },
            {
                "@id": "recordings:2601",
                "@type": "wd:Q3302947",
                "P175": "The Crickard Brothers",
                "P1476": "Musiques Traditionnelles D'Irlande",
                "P2635": 9
            },
            {
                "@id": "recordings:1573",
                "@type": "wd:Q3302947",
                "P175": "The Culchies",
                "P1476": "Bruscar B\u00e1n",
                "P2635": 13
            },
            {
                "@id": "recordings:1255",
                "@type": "wd:Q3302947",
                "P175": "The Dubliners",
                "P1476": "Celebration CD 1",
                "P2635": 4
            },
            {
                "@id": "recordings:5355",
                "@type": "wd:Q3302947",
                "P175": "The Esker Riada C\u00e9il\u00ed Band",
                "P1476": "Come West along the Road",
                "P2635": 4
            },
            {
                "@id": "recordings:5465",
                "@type": "wd:Q3302947",
                "P175": "The Flying Toads",
                "P1476": "Warts 'n All",
                "P2635": 2
            },
            {
                "@id": "recordings:7179",
                "@type": "wd:Q3302947",
                "P175": "The Gallowglass C\u00e9il\u00ed Band",
                "P1476": "Irish Dancing Time",
                "P2635": 9
            },
            {
                "@id": "recordings:3237",
                "@type": "wd:Q3302947",
                "P175": "The Irish Experience",
                "P1476": "Green Energy",
                "P2635": 12
            },
            {
                "@id": "recordings:6876",
                "@type": "wd:Q3302947",
                "P175": "The JSD Band",
                "P1476": "Country Of The Blind",
                "P2635": 2
            },
            {
                "@id": "recordings:2113",
                "@type": "wd:Q3302947",
                "P175": "The Lahawns with Andrew Mac Namara",
                "P1476": "Live At Winkles",
                "P2635": 14
            },
            {
                "@id": "recordings:4030",
                "@type": "wd:Q3302947",
                "P175": "The Liverpool C\u00e9il\u00ed Band",
                "P1476": "Champions Twice",
                "P2635": 4
            },
            {
                "@id": "recordings:4345",
                "@type": "wd:Q3302947",
                "P175": "The Ned Devines",
                "P1476": "Live at Finnegan's Wake",
                "P2635": 3
            },
            {
                "@id": "recordings:429",
                "@type": "wd:Q3302947",
                "P175": "The Nettles",
                "P1476": "The Nettles",
                "P2635": 2
            },
            {
                "@id": "recordings:5064",
                "@type": "wd:Q3302947",
                "P175": "The Shaskeen C\u00e9il\u00ed Band, Malachy Doris C\u00e9il\u00ed Band, The Pride of Erin C\u00e9il\u00ed Band",
                "P1476": "La Vera Musica C\u00e9il\u00ed Irlandese",
                "P2635": 11
            },
            {
                "@id": "recordings:2147",
                "@type": "wd:Q3302947",
                "P175": "The Tulla C\u00e9il\u00ed Band",
                "P1476": "40th Anniversary 1946 - 1986",
                "P2635": 9
            },
            {
                "@id": "recordings:894",
                "@type": "wd:Q3302947",
                "P175": "The Tulla C\u00e9il\u00ed Band",
                "P1476": "A Celebration Of 50 Years",
                "P2635": 9
            },
            {
                "@id": "recordings:1425",
                "@type": "wd:Q3302947",
                "P175": "The Tulla C\u00e9il\u00ed Band",
                "P1476": "Echoes Of Erin",
                "P2635": 7
            },
            {
                "@id": "recordings:5876",
                "@type": "wd:Q3302947",
                "P175": "Theresa O'Grady",
                "P1476": "BANJO'ista",
                "P2635": 12
            },
            {
                "@id": "recordings:4274",
                "@type": "wd:Q3302947",
                "P175": "Threepenny Bit",
                "P1476": "Something...",
                "P2635": 7
            },
            {
                "@id": "recordings:5579",
                "@type": "wd:Q3302947",
                "P175": "Tom Byrne and Tom McCaffrey",
                "P1476": "Irish Music from Cleveland",
                "P2635": 17
            },
            {
                "@id": "recordings:7687",
                "@type": "wd:Q3302947",
                "P175": "Tom Doherty",
                "P1476": "Dance Sean N\u00f3s",
                "P2635": 1
            },
            {
                "@id": "recordings:1210",
                "@type": "wd:Q3302947",
                "P175": "Tom Doherty",
                "P1476": "Take The Bull By The Horns",
                "P2635": 11
            },
            {
                "@id": "recordings:325",
                "@type": "wd:Q3302947",
                "P175": "Tony MacMahon",
                "P1476": "Traditional Irish Accordion",
                "P2635": 1
            },
            {
                "@id": "recordings:6778",
                "@type": "wd:Q3302947",
                "P175": "Toyota C\u00e9il\u00ed Band",
                "P1476": "Gathering Cloud",
                "P2635": 8
            },
            {
                "@id": "recordings:5312",
                "@type": "wd:Q3302947",
                "P175": "Turlach Boylan",
                "P1476": "Lift",
                "P2635": 11
            },
            {
                "@id": "recordings:4984",
                "@type": "wd:Q3302947",
                "P175": "Urban Celtic",
                "P1476": "Urban Celtic",
                "P2635": 2
            },
            {
                "@id": "recordings:5906",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "\"Gort Tape\" CD 2 of 2",
                "P2635": 5
            },
            {
                "@id": "recordings:431",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Celtic Ceili",
                "P2635": 6
            },
            {
                "@id": "recordings:7167",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Celtic Jigs & Reels",
                "P2635": 2
            },
            {
                "@id": "recordings:5848",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Ceol na nOg",
                "P2635": 1
            },
            {
                "@id": "recordings:2607",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Ceol Tigh Neachtain - Music From Galway",
                "P2635": 7
            },
            {
                "@id": "recordings:5407",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Experience Ireland : Disc #1",
                "P2635": 15
            },
            {
                "@id": "recordings:4451",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Fishguard Folk - On a Sunday",
                "P2635": 14
            },
            {
                "@id": "recordings:1983",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "In The Footsteps Of Coleman",
                "P2635": 17
            },
            {
                "@id": "recordings:6874",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Irish Ceili - The Essential Collection (Irish Dance Music)",
                "P2635": 17
            },
            {
                "@id": "recordings:4404",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Irish Jigs & Reels",
                "P2635": 10
            },
            {
                "@id": "recordings:5359",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "It Was Great Altogether!  ~  CD 1 of 3",
                "P2635": 28
            },
            {
                "@id": "recordings:5343",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "It Was Mighty : CD #2",
                "P2635": 13
            },
            {
                "@id": "recordings:1032",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Music For The Sets Volume 3: Pay The Piper",
                "P2635": 12
            },
            {
                "@id": "recordings:4629",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Nights in Shanaglish",
                "P2635": 16
            },
            {
                "@id": "recordings:2516",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "Paddy And Bridget And Their Great Friends 2",
                "P2635": 1
            },
            {
                "@id": "recordings:3070",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "The Blackberry Blossom - Celtic Jigs & Reels",
                "P2635": 2
            },
            {
                "@id": "recordings:3070",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "The Blackberry Blossom - Celtic Jigs & Reels",
                "P2635": 11
            },
            {
                "@id": "recordings:2492",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "The Coleman Archive Volume 2: The Home Place",
                "P2635": 17
            },
            {
                "@id": "recordings:2492",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "The Coleman Archive Volume 2: The Home Place",
                "P2635": 19
            },
            {
                "@id": "recordings:1460",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "The Real Reels Of Ireland",
                "P2635": 17
            },
            {
                "@id": "recordings:4914",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "The Stockport Sea",
                "P2635": 1
            },
            {
                "@id": "recordings:5316",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "We're Irish Still",
                "P2635": 1
            },
            {
                "@id": "recordings:5316",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "We're Irish Still",
                "P2635": 4
            },
            {
                "@id": "recordings:5316",
                "@type": "wd:Q3302947",
                "P175": "Various Artists",
                "P1476": "We're Irish Still",
                "P2635": 24
            },
            {
                "@id": "recordings:6444",
                "@type": "wd:Q3302947",
                "P175": "Vince Collins",
                "P1476": "Over Home",
                "P2635": 11
            },
            {
                "@id": "recordings:3505",
                "@type": "wd:Q3302947",
                "P175": "Wendy MacIsaac",
                "P1476": "The 'Reel' Thing",
                "P2635": 6
            },
            {
                "@id": "recordings:6430",
                "@type": "wd:Q3302947",
                "P175": "Wild Clover Band",
                "P1476": "Behind The Blarney",
                "P2635": 2
            },
            {
                "@id": "recordings:1446",
                "@type": "wd:Q3302947",
                "P175": "William Sullivan",
                "P1476": "Traditional Irish Music",
                "P2635": 33
            }
        ],
        "P9533": [
            {
                "@id": "https://thesession.org/tunes/1#setting1",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2001-05-14T18:45:18",
                "P50": "Jeremy"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting12342",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Eminor",
                "P577": "2002-06-11T15:43:50",
                "P50": "donnchad"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting12343",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Eminor",
                "P577": "2008-06-15T13:53:38",
                "P50": "middlefaster"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting20796",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2013-02-01T03:04:27",
                "P50": "Edgar Bolton"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting20960",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2013-02-17T18:29:47",
                "P50": "sebastian the m3g4p0p"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting21423",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Eminor",
                "P577": "2013-04-15T13:30:56",
                "P50": "Edgar Bolton"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting22061",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2013-08-03T07:16:42",
                "P50": "Tate"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting23915",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2014-04-03T21:29:58",
                "P50": "ceolachan"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting24552",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2014-07-24T14:10:21",
                "P50": "eamonn barr"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting25140",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2014-11-13T01:59:23",
                "P50": "JACKB"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting29823",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2017-02-12T22:50:50",
                "P50": "litewave27"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting31475",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2017-12-11T10:35:07",
                "P50": "Sergei Ejov"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting39518",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2020-11-10T09:40:05",
                "P50": "GraefinZahl"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting39604",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2020-11-20T17:10:55",
                "P50": "Anonymous_Piper"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting40038",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2021-01-03T18:07:01",
                "P50": "Michael Eskin"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting41887",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2021-09-05T23:38:46",
                "P50": "shanachie"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting44243",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2022-06-29T20:38:40",
                "P50": "Blunty026"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting44659",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2022-08-27T19:04:59",
                "P50": "Blunty026"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting45226",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Edorian",
                "P577": "2022-10-31T22:19:36",
                "P50": "Madeleine Townley"
            },
            {
                "@id": "https://thesession.org/tunes/1#setting46013",
                "@type": "wd:Q113899068",
                "P136": "https://thesession.org/tunes/search?type=reel",
                "P3440": "4/4",
                "P826": "Ddorian",
                "P577": "2023-01-29T13:31:02",
                "P50": "PhilPontoise"
            }
        ]
    }

with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))