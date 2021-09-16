from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from datetime import date
from wtforms.validators import DataRequired, Length


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Sign up')


class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


class LogForm(FlaskForm):
    date = DateField('Date: Year-Month-Day', default=date.today(),
                     validators=[DataRequired(message='Invalid date format')])
    company = StringField('Company', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Save')


class ViewForm(FlaskForm):
    time = SelectField('How long would you like this log to capture?',
                       choices=['1 month', '3 months', '6 months', '1 year', 'All applications'],
                       validators=[DataRequired()])
    submit = SubmitField('Save')
