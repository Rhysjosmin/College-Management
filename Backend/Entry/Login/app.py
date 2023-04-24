from flask import Blueprint
import mysql.connector

Login=Blueprint('Login',__name__)


@Login.route('/<StudentName>/<RollNumber>/', methods=['GET'])
def Login(StudentName, RollNumber):
    conn = SQL.connect(host='localhost', password='example-password',
                                 user='abstract-programmer',
                                 database = 'Student_Verification')

    cursor = conn.cursor()

    query = f"SELECT * FROM Verify_Details WHERE StudentName = {StudentName} AND RollNumber = {RollNumber} "
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
         return({'found':True})

    else:
        return({'found':False})

        