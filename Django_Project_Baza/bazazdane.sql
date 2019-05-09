--
-- Plik wygenerowany przez SQLiteStudio v3.2.1 dnia N maj 5 09:38:09 2019
--
-- Użyte kodowanie tekstu: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabela: Forms
CREATE TABLE Forms (id INTEGER PRIMARY KEY AUTOINCREMENT, Code_name TEXT, Current_Shoots INTEGER, Total_Shoots INTEGER, Max_Shoots INTEGER, Status INTEGER, Type_Type INTEGER REFERENCES Type (ID));
INSERT INTO Forms (id, Code_name, Current_Shoots, Total_Shoots, Max_Shoots, Status, Type_Type) VALUES (1, 'F106 1819x', 250, 876578, 750, 1, 1);

-- Tabela: Machine
CREATE TABLE Machine (id INTEGER PRIMARY KEY AUTOINCREMENT, Code_Name TEXT, Name TEXT, Status INTEGER, Form_Forms INTEGER REFERENCES Forms (id), Current_Shoots INTEGER, Total_Shoots INTEGER, Production_id INTEGER);
INSERT INTO Machine (id, Code_Name, Name, Status, Form_Forms, Current_Shoots, Total_Shoots, Production_id) VALUES (1, 'XDM 1001', 'LP1', 1, 1, 250, 78689, 1);

-- Tabela: Production
CREATE TABLE Production (id INTEGER PRIMARY KEY AUTOINCREMENT, shift_date DATE, Machine_Machine INTEGER REFERENCES Machine (id), Production_Value INTEGER, Worker INTEGER);

-- Tabela: Project
CREATE TABLE Project (ID INTEGER PRIMARY KEY AUTOINCREMENT, Project_Name TEXT (30), SOP_Date DATE);
INSERT INTO Project (ID, Project_Name, SOP_Date) VALUES (1, 'Yaris', '2015-02-02');

-- Tabela: Type
CREATE TABLE Type (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Type_ID TEXT, Forms_id INTEGER, Project_Project INTEGER REFERENCES Project (ID));
INSERT INTO Type (ID, Name, Type_ID, Forms_id, Project_Project) VALUES (1, 'Yaris', '751F', 1, 1);

-- Tabela: User
CREATE TABLE User (personal_ID TEXT PRIMARY KEY, Level NUMERIC REFERENCES User_Level (id));
INSERT INTO User (personal_ID, Level) VALUES ('p02545', 4);
INSERT INTO User (personal_ID, Level) VALUES ('p00244', 2);

-- Tabela: User_Level
CREATE TABLE User_Level (id INTEGER PRIMARY KEY AUTOINCREMENT, Level TEXT);
INSERT INTO User_Level (id, Level) VALUES (0, 'Admin');
INSERT INTO User_Level (id, Level) VALUES (1, 'Manager');
INSERT INTO User_Level (id, Level) VALUES (2, 'Supervisor');
INSERT INTO User_Level (id, Level) VALUES (3, 'MNX');
INSERT INTO User_Level (id, Level) VALUES (4, 'User');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
