from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "kfojashliojdsoif"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://stqtbzrcbusesa:f0511cbb1af45509bc33ca34d68904e9efd7f70a00ba19474922165dd4eadd6b@ec2-54-221-220-59.compute-1.amazonaws.com:5432/d80ktb49j3rq66'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER="./app/static/uploads"
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
