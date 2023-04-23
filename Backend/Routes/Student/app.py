from flask import Blueprint
import mysql.connector
from Config import Config
Student=Blueprint('Student', __name__)


@Student.route('/List')
def List():
    
    
    DatabaseConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT",
        database="StudentDB"
        
    )
  
    Database = DatabaseConnection.cursor()
    
 
    
    Database.execute("SELECT * FROM Student")

    Result = Database.fetchall()

      
    return (Result)