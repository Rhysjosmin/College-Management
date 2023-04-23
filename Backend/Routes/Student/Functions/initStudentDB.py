import mysql.connector

DatabaseConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="StudentDB"

)
Database=DatabaseConnection.cursor()

sql = "INSERT INTO Student (id , Name , Year , Department ) VALUES (%s,%s,%s,%s)"
val = [
   (1 , 'Rhys' , 1 , 'Computer') ,
   (2 , 'Samuel' , 2 , 'Electronics') ,
   (3 , 'Smita' , 4 , 'Mechanical') ,
   (4 , 'Mathias' , 2 , 'Electronics') ,
   (5 , 'Joseph' , 1 , 'Computer') ,
   (6 , 'Terrence' , 1 , 'Civil') ,
   (7 , 'Abigail' , 3 , 'Electronics') ,
   (8 , 'Emily' , 1 , 'Civil') ,
   (9 , 'April' , 4 , 'Computer') ,
   (10 , 'May' , 4 , 'Civil') ,
   (11, 'June' , 2 , 'Mechanical') ,
   (12 , 'July' , 1 , 'Electronics') ,
]

Database.executemany(sql, val)
DatabaseConnection.commit()