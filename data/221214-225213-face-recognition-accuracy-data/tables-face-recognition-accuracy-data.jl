{"name": "Algorithm", "description": "This table contains information about the facial recognition algorithm being tested", "columns": "Algorithm_ID (PK), Algorithm_Name, Program_Language, Date_Created, Last_Updated."}
{"name": "Data Set", "description": "This table contains information about the data set used for testing the accuracy of the facial recognition algorithms", "columns": "DataSet_ID (PK), DataSet_Name, Number_of_Images, Facial_Features, Date_Created, Last_Updated. "}
{"name": "Accuracy Results", "description": "This table contains the accuracy results of each facial recognition algorithm on each data set", "columns": "Result_ID (PK), Algorithm_ID (FK), DataSet_ID (FK), Percent_Correct, Date_Created, Last_Updated."}
{"name": "User Information", "description": "This table contains information about the users involved in testing the facial recognition algorithms", "columns": "User_ID (PK), First_Name, Last_Name, Age, Gender, Face_Blindness, Date_Created, Last_Updated. "}
{"name": "Test Sessions", "description": "This table contains information about each test session where a user tested a facial recognition algorithm on a given data set", "columns": "Session_ID (PK), User_ID (FK), Algorithm_ID (FK), DataSet_ID (FK), DateTimeStarted, DateTimeEnded. "}
{"name": "Results by User", "description": "This table contains the accuracy results broken down by individual user who tested the facial recognition algorithms", "columns": "ResultByUser_ID (PK), Session_ID (FK), User_ID (FK), Algorithm_ID (FK), DataSet_ID (FK), PercentCorrect, DateTimeStarted, DateTimeEnded. "}
{"name": "Metadata", "description": "This table contains additional metadata associated with each test session and accuracy result", "columns": "MetaData_ID (PK), Session/ResultByUser ID (FK), Environment(e.g., lighting conditions, location info etc.), AdditionalInfo(e.g., notes from testers regarding any irregularities or issues encountered during testing)."}