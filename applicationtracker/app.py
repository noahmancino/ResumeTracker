from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import configparser
from applicationtracker import forms

config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)
app.config["SECRET_KEY"] = config["APP"]["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE"]["URI"]
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Application', backref='applicant', lazy=True)

    def __repr__(self):
        return f'User({self.username})'


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(75), nullable=False)
    company = db.Column(db.String(75), nullable=False)
    position = db.Column(db.String(75), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Application({self.company}, {self.position}, {self.date.strftime("%m/%d/%Y")}'


@app.route('/')
def home_route():
    '''
    if current_user.is_authenticated:
         return render_template("main_for_user.html")
    else:
         return render_template("main_for_anonymous.html")
    '''
    form = forms.SignUpForm()
    return render_template("entry.html", form=form, page={"title": "Sign in"})


@app.route('/sign-in')
def sign_in():
    form = forms.SignInForm()
    return render_template("entry.html", form=form, page={"title": "Sign in"})


@app.route('/register', methods=['GET'])
def register():
    form = forms.SignUpForm()
    return render_template("entry.html", form=form, page={"title": "Sign up"})


@app.route('/log', methods=['GET', 'POST'])
def log():
    form = forms.LogForm()
    if form.validate():
        print('hello')
    return render_template("log.html", form=form)


@app.route('/view', methods=['GET', 'POST'])
def view():
    form = forms.ViewForm()
    if form.validate():
        print('hello')
    return render_template("view.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
