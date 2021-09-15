from applicationtracker import app
import applicationtracker.forms as forms
from flask import render_template


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