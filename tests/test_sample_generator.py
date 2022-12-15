from sample_peyote import SampleGenerator

queued_api_responses = [
    """1. Bee Population Data: This dataset would contain information about bee population numbers, such as the total number of bees in a given area and the amount of new bees added to that population each year. It could be used to track changes in bee populations over time and study how different factors affect bee populations.
2. Pollen Collection Data: This dataset would contain information about how much pollen is collected by individual bees and the types of flowers they are collecting it from. It could be used to analyze which flowers are most attractive to bees, and how pollination patterns vary with different environmental conditions.
3. Bee Behavior Data: This dataset would contain data on the behaviors of individual bees, such as how long they spend foraging, what type of food they prefer, and how far they travel while searching for food. It could be used to better understand bee behavior and identify potential areas where their behavior needs to be changed or managed in order to protect them.
4. Bee Productivity Data: This dataset would contain information about the productivity of individual bees, such as the amount of honey they produce and the rate at which they produce it. It could be used to analyze the efficiency and effectiveness of beekeeping practices, as well as identify ways to increase productivity.
5. Mite Infestation Data: This dataset would contain information about mite infestations in bee colonies, such as the number of mites present and the level of damage caused by them. It could be used to monitor mite levels in bee colonies and develop strategies for managing infestations.
""",
    """1. Bee Foraging Data: This table contains data about the foraging activities of bees. Columns: Location (foreign key to Location table), Plant Species (foreign key to Plant Species table), Distance Travelled, Pollen Collected, Date/Time Captured, Temperature, Humidity.
2. Location: This table contains data about the locations where bee foraging is taking place. Columns: Location ID, Latitude, Longitude, Address, City, State/Province, Country, Timezone.
3. Plant Species: This table contains data about the plant species that bees are gathering from. Columns: Species ID, Common Name, Scientific Name, Flower Color, Nectar Amount, Pollen Amount.
4. Weather Conditions: This table contains data about the weather conditions that bees encounter while foraging. Columns: Weather ID (foreign key to Location table), Date/Time Captured, Temperature, Humidity, Wind Speed, Precipitation Type.
5. Bee Population: This table contains data about the size and composition of bee populations in each location. Columns: Population ID (foreign key to Location table), Number of Bees Observed, Hive Size (Small/Medium/Large).
6. Bee Behavior: This table contains data about the behavior of individual bees while they are foraging. Columns: Behavior ID (foreign key to Bee Foraging Data), Date/Time Captured, Activity (foraging/resting/etc.), Flight Path (straight line/random pattern).
7. Flight Paths: This table contains data about the flight paths of individual bees while they are foraging. Columns: Path ID (foreign key to Bee Behavior), Date/Time Captured, Start Point (Latitude/Longitude), End Point (Latitude/Longitude), Distance Travelled.
""",
    """Location,Plant Species,Distance Travelled,Pollen Collected,Date/Time Captured,Temperature,Humidity
1,Acer pseudoplatanus,1.2 km,15 mg,9/3/2020 09:30,20°C,70%
2,Rosa canina,1.8 km,25 mg,9/3/2020 10:00,21°C,60%
3,Prunus avium,2.5 km,20 mg,9/3/2020 10:30,22°C,50%
4,Rubus fruticosus,3.4 km,10 mg,9/3/2020 11:00,23°C,40%
5,Mentha spicata,2.1 km,20 mg,9/3/2020 11:30,24°C,30%
6,Cichorium intybus,1.9 km,15 mg,9/3/2020 12:00,25°C,20%
7,Ocimum basilicum,2.3 km,25 mg,9/3/2020 12:30,26°C,10%
8,Rumex acetosella,3.6 km,20 mg,9/3/2020 13:00,27°C,5%
9,Achillea millefolium,1.7 km,15 mg,9/3/2020 13:30,28°C,70%
10,Hyacinthoides non-scripta,2.1 km,25 mg,9/3/2020 14:00,29°C,60%
11,Fritillaria meleagris,3.2 km,20 mg,9/3/2020 14:30,30°C,50%
12,Cerastium fontanum,2.6 km,10 mg,9/3/2020 15:00,31°C,40%
13,Galeopsis tetrahit,1.5 km,20 mg,9/3/2020 15:30,32°C,30%
14,Euphorbia helioscopia,2.4 km,15 mg,9/3/2020 16:00,33°C,20%
15,Allium schoenoprasum,3.1 km,25 mg,9/3/2020 16:30,34°C,10%
16,Rumex crispus,1.8 km,20 mg,9/3/2020 17:00,35°C,5%
17,Lamium album,2.7 km,15 mg,9/3/2020 17:30,36°C,70%
18,Ajuga reptans,3.3 km,25 mg,9/3/2020 18:00,37°C,60%
19,Jasione montana,1.9 km,20 mg,9/3/2020 18:30,38°C,50%
20,Lunaria annua,2.5 km,10 mg,9/3/2020 19:00,39°C,40%
""",
    """Location ID,Latitude,Longitude,Address,City,State/Province,Country,Timezone
1,42.085,-85.637,542 W Main St,Kalamazoo,MI,US,America/Detroit
2,40.837,-74.061,1843 Park Ave,Weehawken,NJ,US,America/New_York
3,51.45,-0.972,3 St. James St,London,England,GB,Europe/London
4,43.741,-79.407,2208 Yonge St,Toronto,ON,CA,America/Toronto
5,41.872,-87.624,20 N Wacker Dr,Chicago,IL,US,America/Chicago
6,48.859,2.351,3 Rue de la Paix,Paris,Ile-de-France,FR,Europe/Paris
7,35.679,139.767,1-1-1 Uchisaiwaicho,Tokyo,Tokyo,JP,Asia/Tokyo
8,37.788,-122.406,333 Market St,San Francisco,CA,US,America/Los_Angeles
9,19.432,-99.133,Av. Insurgentes Sur,Mexico City,Mexico City,MX,America/Mexico_City
10,45.516,-73.567,1255 Rue Peel,Montreal,QC,CA,America/Montreal
11,-33.918,18.424,Mouille Point,Cape Town,Western Cape,ZA,Africa/Johannesburg
12,25.793,-80.126,1220 Ocean Dr,Miami Beach,FL,US,America/New_York
13,-22.902,-43.184,Av. Nossa Senhora de Copacabana,Rio de Janeiro,Rio de Janeiro,BR,America/Sao_Paulo
14,37.775,-122.419,1300 Broadway,Oakland,CA,US,America/Los_Angeles
15,55.752,37.619,Kutuzovsky Prospekt,Moscow,Moscow,RU,Europe/Moscow
16,-34.903,138.597,North Terrace,Adelaide,South Australia,AU,Australia/Adelaide
17,40.715,-74.006,1 Wall St,New York,NY,US,America/New_York
18,-36.851,174.763,Victoria St W,Auckland,Auckland,NZ,Pacific/Auckland
19,43.653,-79.383,100 Queen St W,Toronto,ON,CA,America/Toronto
20,-33.867,151.207,1 Macquarie St,Sydney,New South Wales,AU,Australia/Sydney
""",
    """Species ID,Common Name,Scientific Name,Flower Color,Nectar Amount,Pollen Amount
1,Daisy,Bellis perennis,White,High,High
2,Lavender,Lavandula angustifolia,Purple,High,High
3,Sunflower,Helianthus annuus,Yellow,High,High
4,Marigold,Tagetes erecta,Orange,High,High
5,Apple Blossom,Malus domestica,White,Medium,High
6,Lilac,Syringa vulgaris,Purple,Medium,High
7,Rose,Rosa hybrids,Red,Medium,High
8,Camellia,Camellia japonica,White,Low,High
9,Pansy,Viola tricolor,Purple,Low,High
10,Honeysuckle,Lonicera japonica,Yellow,High,Low
11,Buttercup,Ranunculus spp.,Yellow,High,Low
12,Clover,Trifolium spp.,White,Medium,Low
13,Violet,Viola odorata,Purple,Medium,Low
14,Heather,Calluna vulgaris,Purple,Low,Low
15,Foxglove,Digitalis purpurea,Purple,High,Medium
16,Columbine,Aquilegia spp.,Red,High,Medium
17,Lily,Lilium spp.,White,Medium,Medium
18,Aster,Aster spp.,Purple,Low,Medium
19,Dandelion,Taraxacum officinale,Yellow,Low,Medium
20,Crocus,Crocus spp.,Purple,Low,Low
""",
    """Weather ID,Date/Time Captured,Temperature,Humidity,Wind Speed,Precipitation Type
1,2020-06-01 12:00:00,78,60,5,None
2,2020-06-02 13:00:00,82,55,2,Rain
3,2020-06-03 14:00:00,90,45,3,None
4,2020-06-04 15:00:00,77,50,4,Sleet
5,2020-06-05 16:00:00,85,65,6,Snow
6,2020-06-06 17:00:00,80,60,7,Hail
7,2020-06-07 18:00:00,75,70,2,Rain
8,2020-06-08 19:00:00,73,75,3,None
9,2020-06-09 20:00:00,82,80,4,Fog
10,2020-06-10 21:00:00,90,85,6,Sleet
11,2020-06-11 22:00:00,78,90,7,Rain
12,2020-06-12 23:00:00,85,95,2,None
13,2020-06-13 00:00:00,77,60,3,Hail
14,2020-06-14 01:00:00,82,65,4,Snow
15,2020-06-15 02:00:00,90,70,6,None
16,2020-06-16 03:00:00,75,75,7,Fog
17,2020-06-17 04:00:00,73,80,2,Rain
18,2020-06-18 05:00:00,80,85,3,None
19,2020-06-19 06:00:00,78,90,4,Hail
20,2020-06-20 07:00:00,85,95,6,Sleet
""",
    """Population ID,Number of Bees Observed,Hive Size
1,500,Small
2,1000,Medium
3,1500,Large
4,200,Small
5,700,Medium
6,1200,Large
7,250,Small
8,800,Medium
9,1300,Large
10,300,Small
11,900,Medium
12,1400,Large
13,350,Small
14,950,Medium
15,1500,Large
16,400,Small
17,1000,Medium
18,1350,Large
19,450,Small
20,1100,Medium
""",
    """Behavior ID,Date/Time Captured,Activity,Flight Path
1,10/9/2020 11:00,Foraging,Straight Line
2,10/9/2020 11:15,Resting,Straight Line
3,10/9/2020 11:30,Foraging,Random Pattern
4,10/9/2020 11:45,Resting,Random Pattern
5,10/9/2020 12:00,Foraging,Straight Line
6,10/9/2020 12:15,Resting,Straight Line
7,10/9/2020 12:30,Foraging,Random Pattern
8,10/9/2020 12:45,Resting,Random Pattern
9,10/9/2020 13:00,Foraging,Straight Line
10,10/9/2020 13:15,Resting,Straight Line
11,10/9/2020 13:30,Foraging,Random Pattern
12,10/9/2020 13:45,Resting,Random Pattern
13,10/9/2020 14:00,Foraging,Straight Line
14,10/9/2020 14:15,Resting,Straight Line
15,10/9/2020 14:30,Foraging,Random Pattern
16,10/9/2020 14:45,Resting,Random Pattern
17,10/9/2020 15:00,Foraging,Straight Line
18,10/9/2020 15:15,Resting,Straight Line
19,10/9/2020 15:30,Foraging,Random Pattern
20,10/9/2020 15:45,Resting,Random Pattern
""",
    """Path ID,Date/Time Captured,Start Point (Latitude/Longitude),End Point (Latitude/Longitude),Distance Travelled
1,2020-04-17 10:00:00,37.75,-122.45,37.83,-122.27,2.3
2,2020-04-17 10:15:00,37.83,-122.27,37.76,-122.46,1.2
3,2020-04-17 10:30:00,37.76,-122.46,37.78,-122.37,1.7
4,2020-04-17 10:45:00,37.78,-122.37,37.81,-122.44,1.5
5,2020-04-17 11:00:00,37.81,-122.44,37.77,-122.33,2.2
6,2020-04-17 11:15:00,37.77,-122.33,37.83,-122.27,1.8
7,2020-04-17 11:30:00,37.83,-122.27,37.79,-122.43,1.6
8,2020-04-17 11:45:00,37.79,-122.43,37.75,-122.45,1.7
9,2020-04-17 12:00:00,37.75,-122.45,37.82,-122.41,1.6
10,2020-04-17 12:15:00,37.82,-122.41,37.81,-122.44,0.5
11,2020-04-17 12:30:00,37.81,-122.44,37.76,-122.46,1.2
12,2020-04-17 12:45:00,37.76,-122.46,37.79,-122.43,1.6
13,2020-04-17 13:00:00,37.79,-122.43,37.83,-122.27,1.8
14,2020-04-17 13:15:00,37.83,-122.27,37.78,-122.37,1.7
15,2020-04-17 13:30:00,37.78,-122.37,37.76,-122.46,1.2
16,2020-04-17 13:45:00,37.76,-122.46,37.81,-122.44,1.5
17,2020-04-17 14:00:00,37.81,-122.44,37.77,-122.33,2.2
18,2020-04-17 14:15:00,37.77,-122.33,37.83,-122.27,1.8
19,2020-04-17 14:30:00,37.83,-122.27,37.75,-122.45,2.3
20,2020-04-17 14:45:00,37.75,-122.45,37.82,-122.41,1.6
""",
]

def test_end_to_end(monkeypatch):

    def mock__get_openai_response_text(**kwargs):
        return queued_api_responses.pop(0)

    sammy = SampleGenerator(
        run_id="my-run-id",
    )
    monkeypatch.setattr(sammy, '_get_openai_response_text', mock__get_openai_response_text)

    sammy.generate_dataset_idea_list(topic="bees")
    sammy.select_dataset_by_index(index=1)
    sammy.render_markdown()
    sammy.save(path="./test")