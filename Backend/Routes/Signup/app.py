from flask import Blueprint,request
from pymongo import MongoClient
Signup=Blueprint('Signup',__name__)

Client = MongoClient("mongodb://localhost:27017/")
CollegeDB=Client['CollegeDB']
Users=CollegeDB['Users']


@Signup.route('/', methods=['POST'])
def SignupRoute():
    Password=request.json.get('Password')
    Username=request.json.get('Username')
    Email=request.json.get('Email')
    UserType=request.json.get('UserType')
    if(Users.find_one({'Username':Username})):
        return 'Username Already Present'
    else:
        Users.insert_one({'Username':Username,'Email':Email,'Password':Password,'UserType':UserType})
        return 'Done'


        