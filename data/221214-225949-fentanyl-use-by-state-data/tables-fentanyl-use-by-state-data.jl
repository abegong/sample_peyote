{"name": "State_Info", "description": "This table contains information about each state, including population size and geographic area", "columns": "State, Population, Area (sq mi), Population Density (per sq mi), Timestamp."}
{"name": "Fentanyl_Use_By_State", "description": "This table contains fentanyl use statistics for each state", "columns": "State (FK to State_Info table), Age Group, Gender, Number of Users, Timestamp. "}
{"name": "Fentanyl_Usage_Trends", "description": "This table contains trend data on the prevalence of fentanyl use in each state over time", "columns": "State (FK to State_Info table), Year, Number of Users, Timestamp. "}
{"name": "Fentanyl_Abuse_Risk_Factors", "description": "This table contains demographic data on risk factors associated with fentanyl abuse in each state such as poverty level and educational attainment", "columns": "State (FK to State_Info table), Poverty Level, Educational Attainment, Timestamp. "}
{"name": "Drug_Treatment_Centers", "description": "This table contains information on drug treatment centers in each state", "columns": "Center Name, Address, Phone Number, Website URL, State (FK to State_Info table), Services Offered, Timestamp. "}
{"name": "Fentanyl_Related_Deaths", "description": "This table contains information on deaths related to fentanyl use in each state", "columns": "State (FK to State_Info table), Age Group, Gender, Number of Deaths, Cause of Death, Timestamp. "}
{"name": "Law_Enforcement_Data", "description": "This table contains law enforcement data related to fentanyl use in each state such as arrests and seizures", "columns": "State (FK to State_Info table), Arrests/Seizures Made, Type of Offense, Timestamp."}