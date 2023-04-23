from flask import Blueprint
import mysql.connector

Login=Blueprint('Login',__name__)

@Login.route('/<EncryptedUsername>/<EncryptedPassword/<Key>')
def Login():
    
    if User in DB:
        return 'Pass'
    return 'Fail'