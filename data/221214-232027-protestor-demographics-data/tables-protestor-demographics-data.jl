{"name": "Protestor Demographics", "description": "This table contains information about individual protesters", "columns": "Protestor ID, Age, Gender, Race, Ethnicity, Socio-Economic Status, TimeStamp."}
{"name": "Protests", "description": "This table contains information about the specific protests that protesters attended", "columns": "Protest ID, Location, Date and Time, Type of Protest (e.g., peaceful or violent), Number of Participants, TimeStamp. "}
{"name": "Protestor Locations", "description": "This table contains information about where each protester was located during a protest", "columns": "Protestor ID (Foreign key to the Protestor Demographics table), Latitude, Longitude, TimeStamp."}
{"name": "Protestor Interactions", "description": "This table contains information about interactions between protesters at a protest", "columns": "Interaction ID, Participant 1 (Foreign key to the Protestor Demographics table), Participant 2 (Foreign key to the Protestor Demographics table), Nature of Interaction (e.g., friendly/hostile), TimeStamp. "}
{"name": "Protest Outcomes", "description": "This table contains information about the outcomes of individual protests", "columns": "Protest ID (Foreign key to the Protests table), Outcome (e.g., success/failure), Description of Outcome, TimeStamp."}