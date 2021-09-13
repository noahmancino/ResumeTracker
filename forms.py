from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from datetime import date
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')


class SignInForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign in')


class LogForm(FlaskForm):
    date = DateField('Date: Year-Month-Day', default=date.today(),
                     validators=[DataRequired(message='Invalid date format')])
    company = StringField('Company', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    location = StringField('Location')
    submit = SubmitField('Save')
