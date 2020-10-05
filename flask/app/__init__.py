from flask import Flask 
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
admin = Admin()

from app import views

