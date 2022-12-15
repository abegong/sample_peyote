{"name": "Users", "description": "This table contains information on individual users", "columns": "User_id, Username, Age, Gender, Location, Interests, Timestamp (created)."}
{"name": "Followers", "description": "This table contains information on who follows whom", "columns": "Follower_id, Following_id (foreign key to User table), Timestamp (followed)."}
{"name": "Posts", "description": "This table contains information on posts made by users", "columns": "Post_id, User_id (foreign key to User table), Content, Likes, Comments, Timestamp (created)."}
{"name": "Reactions", "description": "This table contains information on reactions that users have to posts", "columns": "Reaction_id, Post_id (foreign key to Posts table), User_id (foreign key to User table), Type of reaction (like/comment/share etc.), Timestamp (reacted)."}
{"name": "Hashtags", "description": "This table contains information on hashtags used in posts", "columns": "Hashtag_id, Post_id (foreign key to Posts table), Tag, Timestamp (added). "}
{"name": "Engagement", "description": "This table contains aggregate data on user engagement with posts and other content", "columns": "Engagement_id, User_id (foreign key to User table), Views, Likes, Shares, Comments, Timestamp (updated)."}