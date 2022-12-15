{"name": "Diagnosis Table", "description": "This table contains information about each individual diagnosis", "columns": "Diagnosis_ID (Primary Key), Patient_ID (Foreign Key), Diagnosis_Date, Genetic_Abnormality, Treatment_Received, Timestamp."}
{"name": "Patient Table", "description": "This table contains information about each patient with a Down Syndrome diagnosis", "columns": "Patient_ID (Primary Key), Age, Gender, Race, Location, Timestamp."}
{"name": "Physician Table", "description": "This table contains information about the physicians who diagnose individuals with Down Syndrome", "columns": "Physician_ID (Primary Key), Name, Specialty, Practice_Location, Timestamp."}
{"name": "Hospital Table", "description": "This table contains information about hospitals where Down Syndrome diagnoses are made", "columns": "Hospital_ID (Primary Key), Name, Address, Phone Number, Timestamp. "}
{"name": "Clinical Trial Table", "description": "This table contains information about clinical trials related to Down Syndrome diagnoses and treatments", "columns": "Clinical_Trial_ID (Primary Key), Title, Description, Start Date, End Date, Timestamp."}