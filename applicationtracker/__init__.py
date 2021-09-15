from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)
app.config["SECRET_KEY"] = config["APP"]["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE"]["URI"]
db = SQLAlchemy(app)

import applicationtracker.routes