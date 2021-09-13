from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import configparser
import forms
from flask_login import current_user

config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)
app.config["SECRET_KEY"] = config["APP"]["SECRET_KEY"]
print(config["APP"]["SECRET_KEY"])


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

if __name__ == '__main__':
    app.run(debug=True)
