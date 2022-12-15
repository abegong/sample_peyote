{"name": "Books", "description": "This table contains information about each book in the Goosebumps series", "columns": "Title, Author, Release Date, Description, Genre, Book Cover Image (foreign key to Images table), Timestamps"}
{"name": "Authors", "description": "This table contains information about the authors of the Goosebumps books", "columns": "Author Name, Biography, Nationality, Number of Published Books, Author Photo Image (foreign key to Images table), Timestamps"}
{"name": "Images", "description": "This table contains images related to the Goosebumps books", "columns": "Image URL, Image Type (book cover image or author photo image), Timestamps"}
{"name": "Reviews", "description": "This table contains reviews for each book in the series", "columns": "Reviewer Name, Rating, Review Text, Book (foreign key to Books table), Timestamps"}
{"name": "Ratings", "description": "This table contains ratings for each book in the series", "columns": "User Name, Rating, Book (foreign key to Books table), Timestamps"}