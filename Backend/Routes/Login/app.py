import json
from flask import Blueprint,request
from pymongo import MongoClient
Login=Blueprint('Login',__name__)

Client = MongoClient("mongodb://localhost:27017/")
CollegeDB=Client['CollegeDB']

Users=CollegeDB['Users']


@Login.route('/', methods=['POST'])
def LoginRoute():
    Username=request.json.get('Username')
    Email=request.json.get('Email')
    Password=request.json.get('Password')
    print(Username)
    print(Email)
    print(Password)
    Result=Users.find_one({'Username':Username,'Email':Email,'Password':Password})
    
    if Result:
        Result
        return json.dumps({'Present':'True','UserType':Result['UserType']})
    else:
        return json.dumps({'Present':'False'})
    


        