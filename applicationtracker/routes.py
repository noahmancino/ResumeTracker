from applicationtracker import app, db, bcrypt, login_manager
from flask_login import login_user
import applicationtracker.forms as forms
from applicationtracker.models import User, Application
from flask import render_template, flash, redirect, url_for


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


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home_route'))
        else:
            flash('Could not find that username password combination', 'danger')

    return render_template("entry.html", form=form, page={"title": "Sign in"})


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Your registration was successful, you may now log in', 'success')
        return redirect(url_for('sign_in'))
    return render_template("entry.html", form=form, page={"title": "Sign up"})


@app.route('/log', methods=['GET', 'POST'])
def log():
    form = forms.LogForm()
    if form.validate_on_submit():
        flash('application saved', 'success')
    return render_template("log.html", form=form)


@app.route('/view', methods=['GET', 'POST'])
def view():
    form = forms.ViewForm()
    if form.validate_on_submit():
        pass
    return render_template("view.html", form=form)