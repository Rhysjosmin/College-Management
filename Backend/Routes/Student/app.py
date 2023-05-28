import json

from flask import Blueprint, request
from pymongo import MongoClient
from gridfs import GridFS
from Config import Config
Student=Blueprint('Student', __name__)
import pandas as pd

Client = MongoClient("mongodb://localhost:27017/")
CollegeDB=Client['CollegeDB']

fs = GridFS(CollegeDB)
Announcements=CollegeDB['Announcements']
Users=CollegeDB['Users']

@Student.route('/Details/Add',methods=['POST'])
def Add_Details():
    Username=request.json.get('Username')
    Param=request.json.get('Param')
    Value=request.json.get('Value')
    Users.find_one_and_update({'Username': Username}, {'$set': {Param: Value}})
    return 'Added'



@Student.route('/Details/Add/All',methods=['POST'])
def Add_All_Details():
    Username=request.json.get('Username')
    RollNumber=request.json.get('RollNumber')
    Mentor=request.json.get('Mentor')
    Department=request.json.get('Department')
    Year=request.json.get('Year')
    CGPA=request.json.get('CGPA')
    SGPA=request.json.get('SGPA')
    
    Users.find_one_and_update({'Username': Username}, {'$set': {
        'RollNumber':RollNumber,
        'Mentor':Mentor,
        'Department':Department,
        'Year':Year,
        'CGPA':CGPA,
        'SGPA':SGPA
    }})
    return "Added"

@Student.route('/Details/Add/CSV',methods=['POST'])
def Details_From_CSV():
    file = request.files['file']
    print(file.mimetype)
  
    if(file.mimetype=='text/csv'):
        Already=[]
        df = pd.read_csv(file,encoding='latin-1')
        values = df.values.tolist()
        for User in values:
            if(not(Users.find_one({'Username':User[0]}))):
                Users.insert_one({
                    "Username":User[0],
                    "RollNumber":User[1],
                    "Department":User[2],
                    "Year":User[3],
                    "Mentor":User[4],
                    "CGPA":User[5],
                    "SGPA":User[6],
                    "Email":User[7],
                    "Password":User[8],
                    "UserType":User[9],                
                })
            else:
                Already.append(User[0])
        
        return json.dumps(Already)

    return 'Fail'

@Student.route('/ProfilePic/Add/<Username>',methods=["POST"])
def AddProfilePic(Username):
    Image = request.files['Image']
    Image_Id = fs.put(Image)
    Users.find_one_and_update({'Username':Username},{'$set':{'Image':Image_Id}})
    print(Image_Id)
    return 'Added Profile Picture'

@Student.route('/Announcements')
def ViewAnnouncements():
    Announcement_List=Announcements.find()
    List=[]
    for Item in Announcement_List:
        List.append(Item['Title'])
    print(List)
    return json.dumps({'Items':List})