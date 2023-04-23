import mysql.connector
Database_to_Be_Created = 'StudentDB'
DeleteDATABASE=False
CreateDATABASE=False

if DeleteDATABASE:
    DatabaseConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT",
    )
    Database = DatabaseConnection.cursor()
    Database.execute('DROP DATABASE StudentDB')
    DatabaseConnection.commit()
    DatabaseConnection.close()
    
if CreateDATABASE:
        DatabaseConnection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ROOT",
        )
        Database = DatabaseConnection.cursor()
        Database.execute(f"CREATE DATABASE {Database_to_Be_Created}")
        print('Database Created')



try:
    DatabaseConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT",
        database='StudentDB'
    )

    Database = DatabaseConnection.cursor()
    
   
    
    Database.execute(
        f'''CREATE TABLE Student
        (id INT PRIMARY KEY, 
        Name VARCHAR(255), 
        Year INT, 
        Department VARCHAR(255),
        Mentor VARCHAR(255))
        ''')
    DatabaseConnection.commit()
    DatabaseConnection.close()
    print('Done')
except:
    pass
