from flask import Flask
from flask_cors import CORS
from Routes.Student.app import Student
from Routes.Admin.app import Admin
app=Flask(__name__)
cors=CORS(app)
app.register_blueprint(Student,url_prefix='/Student')
app.register_blueprint(Admin,url_prefix='/Admin')


if __name__ =="__main__":
    app.run(debug=True)