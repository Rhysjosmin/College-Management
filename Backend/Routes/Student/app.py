import json
from flask import Blueprint, request
from pymongo import MongoClient
from gridfs import GridFS

from Config import Config
Student=Blueprint('Student', __name__)

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