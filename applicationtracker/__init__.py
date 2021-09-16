from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import configparser
from flask_bcrypt import Bcrypt

config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)
app.config["SECRET_KEY"] = config["APP"]["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE"]["URI"]
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

import applicationtracker.routes