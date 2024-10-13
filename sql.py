import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:
    prefix ='sqlite:///'
else:
    prefix ='sqlite:////'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)#主键
    name = db.Column(db.String(80), unique=True, nullable=False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)

