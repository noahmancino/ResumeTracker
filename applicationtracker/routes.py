from applicationtracker import app, db, bcrypt, login_manager
from flask_login import login_user, current_user, logout_user, login_required
import applicationtracker.forms as forms
from applicationtracker.models import User, Application
from flask import render_template, flash, redirect, url_for
from datetime import date
import pandas as pd


@app.route('/')
def home_route():
    if current_user.is_authenticated:
         return redirect(url_for("log"))
    else:
         return redirect(url_for("register"))


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        flash("You are already logged in", "success")
        return redirect(url_for('log'))

    form = forms.SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Successful login", "success")
            return redirect(url_for('home_route'))
        else:
            flash('Could not find that username password combination', 'danger')

    return render_template("entry.html", form=form, page={"title": "Sign in"})


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in", "success")
        return redirect(url_for('log'))

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
@login_required
def log():
    form = forms.LogForm()
    if form.validate_on_submit():
        application = Application(date=form.date.data, location=form.location.data, position=form.position.data,
                                  company=form.company.data, applicant=current_user)
        db.session.add(application)
        db.session.commit()
        flash('Application saved', 'success')
        return redirect(url_for('log'))
    return render_template("log.html", form=form)


@app.route('/view', methods=['GET', 'POST'])
@login_required
def view():
    def diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    form = forms.ViewForm()
    if form.validate_on_submit():
        time_delta = form.time.data
        applications = db.session.query(Application).filter(Application.applicant == current_user)
        applications = pd.read_sql(applications.statement, db.session.bind)
        applications.drop('user_id', inplace=True, axis=1)
        applications['time_delta'] = applications['date'].apply(lambda x: diff_month(date.today(), x))
        applications.drop('id', inplace=True, axis=1)
        applications.sort_values(by=['date'])
        if time_delta != 'all':
            applications = applications[applications.time_delta <= int(time_delta)]
        applications.drop('time_delta', inplace=True, axis=1)
        return applications.to_html()

    return render_template("view.html", form=form)


#TODO: logging out typically uses post requests, the logout link might get prefetched by browser
@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('home_route'))
