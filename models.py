from flask import Flask
from flask_sqlalchemy import SQLAlchemy

u_id = 1
b_id = 1
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/library"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    category = db.Column(db.String(100), unique=False, nullable=False)
    author = db.Column(db.String(100), unique=False, nullable=False)

class admin_table(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)