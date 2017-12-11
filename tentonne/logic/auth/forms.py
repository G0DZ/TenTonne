from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

from ..models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[a-z]|[A-Z][0-9_.]*', 0,
                                              'letter required')])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm password', validators=[DataRequired(),
                                                            EqualTo('password', message='Passwords must match')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email already used')

    def validate_nickname(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username already used')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('rememberme', default=False)
