CREATE DATABASE Student_Verification;

USE Student_Verification;

CREATE TABLE Verify_Details(
ID INT PRIMARY KEY AUTO_INCREMENT,
Student_Name VARCHAR(200) NOT NULL,
Roll_Number VARCHAR(20) NOT NULL UNIQUE,
Email VARCHAR(200) NOT NULL UNIQUE,
Department VARCHAR(100) NOT NULL
);

INSERT INTO Verify_Details (Student_Name,Roll_Number,Email,Department) VALUES 
('Jonah Smith','547891','jonah@gmail.com','Computer');
INSERT INTO Verify_Details (Student_Name,Roll_Number,Email,Department) VALUES 
('Samantha Jones','478091','sammy@gmail.com','Electronics');
INSERT INTO Verify_Details (Student_Name,Roll_Number,Email,Department) VALUES 
('Alan Cook','964791','alan@gmail.com','Mechanical');
INSERT INTO Verify_Details (Student_Name,Roll_Number,Email,Department) VALUES 
('Bob Floyd','321781','bob@gmail.com','Civil');
INSERT INTO Verify_Details (Student_Name,Roll_Number,Email,Department) VALUES 
('Thomas Cook','654789','thomas@gmail.com','Computer');
INSERT INTO Verify_Details (Student_Name,Roll_Number,Email,Department) VALUES 
('Rosa Denvers','565741','rosa@gmail.com','Civil');


SELECT * FROM Verify_Details;