import json
from flask import Blueprint, request
from pymongo import MongoClient

from Config import Config
Student=Blueprint('Student', __name__)

Client = MongoClient("mongodb://localhost:27017/")
CollegeDB=Client['CollegeDB']

Announcements=CollegeDB['Announcements']
Users=CollegeDB['Users']

@Student.route('/Details/Add',methods=['POST'])
def Add_Details():
    Username=request.json.get('Username')
    Param=request.json.get('Param')
    Value=request.json.get('Value')
    Users.find_one_and_update({'Username': Username}, {'$set': {Param: Value}})
    return 'Added'


@Student.route('/Announcements')
def ViewAnnouncements():
    Announcement_List=Announcements.find()
    List=[]
    for Item in Announcement_List:
        List.append(Item['Title'])
    print(List)
    return json.dumps({'Items':List})