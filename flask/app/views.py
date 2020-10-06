from app import app, admin
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, render_template, request, url_for
from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user

# Configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

app.config['SECRET_KEY'] = 'mysecret' 

db = SQLAlchemy(app)
login = LoginManager(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

# Admin routes

admin.init_app(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))

# User routes

@app.route('/')

def home():

    return render_template("index.html")

@app.route('/login')
def login():
    user = User.query.get(1)
    login_user(user)
    return redirect(url_for('admin.index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))