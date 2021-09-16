from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, ValidationError
from datetime import date
from wtforms.validators import DataRequired, Length
from applicationtracker.models import User

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is not None:
            raise ValidationError("Someone else already has that username")


class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


class LogForm(FlaskForm):
    date = DateField('Date: Year-Month-Day', default=date.today(),
                     validators=[DataRequired(message='Invalid date format')])
    company = StringField('Company', validators=[DataRequired(), Length(max=75)])
    position = StringField('Position', validators=[DataRequired(), Length(max=75)])
    location = StringField('Location', validators=[DataRequired(), Length(max=75)])
    submit = SubmitField('Save')


class ViewForm(FlaskForm):
    time = SelectField('How long would you like this log to capture?',
                       choices=[('1', '1 month'), ('3', '3 months'), ('6', '6 months'), ('12', '1 year'),
                                ('0', 'All applications')],
                       validators=[DataRequired()])
    submit = SubmitField('Save')
