from flask import Flask
from Routes.Student.app import Student

app=Flask(__name__)

app.register_blueprint(Student,url_prefix='/Student')

if __name__ =="__main__":
    app.run(debug=True)