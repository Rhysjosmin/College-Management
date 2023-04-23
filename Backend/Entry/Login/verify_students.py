import mysql.connector as sql

conn = sql.connect(
    host='localhost', 
    password='example-password',
    user='abstract-programmer',
    database = 'Student_verification'
    )

cursor = conn.cursor()

query = "SELECT * FROM Verify_Details WHERE Department = 'Computer'"
cursor.execute(query)


rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()