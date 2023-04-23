import mysql.connector
DatabaseConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="StudentDB"
)
Database = DatabaseConnection.cursor()
Database.execute('DELETE FROM Student;')
DatabaseConnection.commit()
