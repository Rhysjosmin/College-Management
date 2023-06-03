from flask import Blueprint,Response, request
from Config import Config
import json
from pymongo import MongoClient
from gridfs import GridFS
from bson import json_util,ObjectId



Client = MongoClient("mongodb://localhost:27017/")

CollegeDB=Client['CollegeDB']
fs = GridFS(CollegeDB)
CanteenDB=CollegeDB['CanteenDB']
CanteenOrderDB=CollegeDB['CanteenOrderDB']


Canteen=Blueprint('Canteen', __name__)


@Canteen.route('/Menu')
def Menu():
    return json_util.dumps(CanteenDB.find())


@Canteen.route('/AddItem',methods=["POST"])
def AddItem():
    # Name=request.json.get('Name')
    # Price=request.json.get('Price')
    Name=request.form.get('Name')
    Price=request.form.get('Price')
    # Image=request.files['Image']
    # Image_Id = fs.put(Image)
    CanteenDB.insert_one({
            "Name":Name,
            "Price": Price
        })
    return 'Added Item'


@Canteen.route('/AddImage/<Name>',methods=["POST"])
def AddImage(Name):
    Image=request.files['Image']
    Image_Id=fs.put(Image)
    CanteenDB.find_one_and_update({'Name':Name},{'$set':{'Image_ID':Image_Id}})
    return 'Done'


@Canteen.route('/RemoveItem')
def RemoveItem():
    # Has To Have Key to Remove
    return 'Removed Item'

@Canteen.route('/ModifyItem')
def ModifyItem():
    return 'Modified Item'

@Canteen.route('/Placeorder',methods=["POST"])
def PlaceOrder():
    Order=request.form.get('Items')
    Name=request.form.get('Name')
    CanteenOrderDB.insert_one({'Name':Name,"Order":Order})
    return json.dumps({'Response':'OK'})

@Canteen.route('/SeeOrders')
def SeeOrders():
    Orders=CanteenOrderDB.find()
    return json_util.dumps(Orders)