{"name": "State Data", "description": "This table contains data about individual states in the US", "columns": "State Name, Population, Number of Abortions Since 1973, Abortion Rate Per 1000 People, Timestamp."}
{"name": "Public Opinion Polls", "description": "This table contains poll results from different public opinion surveys about abortion since 1973", "columns": "Survey Name, Date of Poll, Percent Pro-Choice, Percent Pro-Life, Total Respondents, Timestamp."}
{"name": "Court Cases", "description": "This table contains information about court cases related to Roe v Wade since 1973", "columns": "Case Name, Year of Decision, Outcome (Pro-Choice/Anti-Choice), Significance to Roe v Wade, State of Origin (Foreign Key to State Table), Timestamp. "}
{"name": "Legislation", "description": "This table contains information about legislation related to abortion since 1973", "columns": "Bill Name, Year Passed, Outcome (Passed/Failed), Significance to Roe v Wade, State (Foreign Key to State Table), Timestamp."}