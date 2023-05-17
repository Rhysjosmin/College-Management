from flask import Blueprint,Response
from Config import Config
import json
Canteen=Blueprint('Canteen', __name__)

@Canteen.route('/Menu')
def Menu():
    menuFlie=open('Backend/DB/CanteenMenu.json')
    menu=json.load(menuFlie)
    return json.dumps(menu)


@Canteen.route('/AddItem')
def AddItem():
    # Has To Have Key to add
    return 'Added Item'

@Canteen.route('/RemoveItem')
def RemoveItem():
    # Has To Have Key to Remove
    return 'Removed Item'

@Canteen.route('/ModifyItem')
def ModifyItem():
    return 'Modified Item'