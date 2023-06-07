import json
from flask import Flask, url_for
from bson import json_util,ObjectId
from flask_cors import CORS
from gridfs import GridFS
from pymongo import MongoClient
from Routes.Student.app import Student
from Routes.Admin.app import Admin
from Routes.Canteen.app import Canteen
from Routes.Login.app import Login
from Routes.Signup.app import Signup

app=Flask(__name__)
cors=CORS(app)

app.register_blueprint(Student,url_prefix='/Student')
app.register_blueprint(Canteen,url_prefix='/Canteen')
app.register_blueprint(Admin,url_prefix='/Admin')
app.register_blueprint(Login,url_prefix='/Login')
app.register_blueprint(Signup,url_prefix='/Signup')

Client = MongoClient("mongodb://localhost:27017/")

CollegeDB=Client['CollegeDB']
fs = GridFS(CollegeDB)
Users=CollegeDB['Users']


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route('/')
def index():
    links = []
    l=[]
    for rule in app.url_map.iter_rules():
        l.append(rule.endpoint)
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(f'<a href="{url}">{rule.endpoint}</a>')
    string = ''
    for link in links:
        string = string+link+'</br>'
    return json.dumps(l)

@app.route('/Databases')
def Databases():
    return json.dumps(CollegeDB.list_collection_names())

@app.route('/DeleteCollection/<Collection>',methods=['GET'])
def DeleteCollection(Collection):
    CollegeDB.drop_collection(Collection)
    return 'Dropped '+Collection

@app.route('/UserData/<Username>',methods=['GET'])
def getUserData(Username):
    Data=Users.find_one({'Username':Username})
    return json_util.dumps(Data)

@app.route('/GetImage/<ImageID>',methods=['GET'])
def getImage(ImageID):
    Data=fs.get(ObjectId(ImageID)).read() 
    return json_util.dumps(Data)

@app.route('/StudentDetails')
def StudentDetails():
    return json_util.dumps(Users.find({ "UserType": "Student"}))
if __name__ =="__main__":
    app.run(debug=True, port=5001)



