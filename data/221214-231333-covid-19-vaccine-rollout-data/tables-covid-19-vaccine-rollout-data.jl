{"name": "Vaccine_Administration", "description": "This table contains information about each individual vaccine administration", "columns": "Patient_ID, Vaccine_Name, Date_Administered, Location, Dose_Number, Side_Effects (foreign key to Side_Effects table), Timestamp. "}
{"name": "Patients", "description": "This table contains information about each patient who receives a vaccine", "columns": "Patient_ID, Age, Gender, Medical_Conditions (foreign key to Medical_Conditions table), Vaccines_Received (foreign key to Vaccine_Administration table), Timestamp."}
{"name": "Side_Effects", "description": "This table contains information about reported side effects from the vaccine", "columns": "Side_Effect_ID, Side_Effect_Name, Severity (Low/Medium/High), Vaccine_Administration (foreign key to Vaccine Administration table), Timestamp. "}
{"name": "Medical_Conditions", "description": "This table contains information about medical conditions of patients who receive the vaccine", "columns": "Condition_ID, Condition_Name, Patient (foreign key to Patients table), Timestamp."}