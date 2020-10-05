from app import app, admin
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin

# Configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

# Admin routes

admin.init_app(app)
admin.add_view(ModelView(User, db.session))

# User routes

@app.route('/')

def home():

    return render_template("index.html")
