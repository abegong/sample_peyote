{"name": "Characters", "description": "This table contains information about characters in Shakespeare's works", "columns": "character_id (primary key), character_name, play_id (foreign key to Plays table), gender, description, created_at, updated_at"}
{"name": "Plays", "description": "This table contains information about plays by Shakespeare", "columns": "play_id (primary key), play_title, genre, year_written, language, created_at, updated_at"}
{"name": "Scenes", "description": "This table contains information about scenes within a play", "columns": "scene_id (primary key), play_id (foreign key to Plays table), scene_number, setting, description, created_at, updated_at"}
{"name": "Character Interactions", "description": "This table contains information about interactions between characters in a given scene", "columns": "interaction_id (primary key), character1_id (foreign key to Characters table), character2_id (foreign key to Characters table), scene_id (foreign key to Scenes table), interaction_type, dialogue, created_at, updated_at"}
{"name": "Character Relationships", "description": "This table contains information about the relationships between characters in a given play", "columns": "relationship_id (primary key), character1_id (foreign key to Characters table), character2_id (foreign key to Characters table), relationship_type, description, created_at, updated_at"}