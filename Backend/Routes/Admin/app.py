from flask import Blueprint, render_template, request
import pandas as pd
from pymongo import MongoClient


Client = MongoClient("mongodb://localhost:27017/")
CollegeDB=Client['CollegeDB']
Announcements=CollegeDB['Announcements']

Admin=Blueprint('Admin',__name__,template_folder='templates')




@Admin.route('/UploadStudentCredentials', methods=['GET', 'POST'])
def uploadFile():
    # insertionError=False
    # if request.method == 'POST':
    #   # upload file flask
    #     f = request.files.get('file')
    #     df=  pd.read_csv(f).values.tolist()
    #     try:
    #         insertInStudentDB(list(df))
    #     except:
    #         insertionError=True
    #     return render_template('index.html',imported=True,insertionError=insertionError)
    # return render_template("index.html", imported=False,insertionError=insertionError)
    return render_template("index.html", imported=False,insertionError='insertionError')

def insertInStudentDB(CSV):
    # DatabaseConnection = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="ROOT",
    #     database="StudentDB"
    # )
    # Database=DatabaseConnection.cursor()
    # sql = "INSERT INTO Student (id , Name , Year , Department, Mentor ) VALUES (%s,%s,%s,%s,%s)"
    # val = [ ]

    # for Student in CSV:
    #     val.append((Student[0],Student[1],Student[2],Student[3],Student[4]))
    # Database.executemany(sql, val)
    # DatabaseConnection.commit()
    return '0'


@Admin.route('/Announcement/Add',methods=['POST'])
def AddAnnouncement():

    Title=request.json.get('Title')
    Body=request.json.get('Body')

    Announcements.insert_one({'Title':Title,'Body':Body})


    return 'Done'

