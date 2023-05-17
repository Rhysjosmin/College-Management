from flask import Flask
from flask_cors import CORS
from Routes.Student.app import Student
from Routes.Admin.app import Admin
from Routes.Canteen.app import Canteen
app=Flask(__name__)
cors=CORS(app)
app.register_blueprint(Student,url_prefix='/Student')
app.register_blueprint(Canteen,url_prefix='/Canteen')
app.register_blueprint(Admin,url_prefix='/Admin')

@app.route('/')
def Menu():
    return 'o'

# if __name__ =="__main__":
#     app.run(debug=True)


