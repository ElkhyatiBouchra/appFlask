from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , BooleanField
from wtforms.validators import InputRequired ,Email , Length

from __main__ import db




### models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password =db.Column(db.String(80))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)] )
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(),Email(message='Invalid email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)] )   
