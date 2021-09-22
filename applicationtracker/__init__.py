from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

'''
config = configparser.ConfigParser()
config.read("config.ini")
'''

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('APP_SECRET_KEY', 'default')
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI', "no!!!!")
db = SQLAlchemy(app)
db.create_all()
print(app.config["SQLALCHEMY_DATABASE_URI"])
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in'
login_manager.login_message_category = 'info'

import applicationtracker.routes


def getApp():
    return app
