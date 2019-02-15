# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:40:42 2019

@author: Elkhyati bouchra
"""
from flask import Flask ,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , BooleanField
from wtforms.validators import InputRequired ,Email , Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecrpet'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/Elkhyati bouchra/Documents/appFlask/database.db'
Bootstrap(app)  
db = SQLAlchemy(app)
from model import User , LoginForm ,RegisterForm



 #### mapping   
    
@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    msg_err=" "
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return render_template("dashboard.html",user = user)
        else :
            msg_err="incorrect user name or password"        
    return render_template('login.html',form=form,msg_err=msg_err)

@app.route('/signup',methods=['GET','POST']) 
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user= User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user has b een created! </h1>'
        #return '<h1>' + form.username.data + ' '+form.email.data+' '+ form.password.data +'</h1>'
    return render_template('signup.html',form=form) 
    
@app.route('/dashboard')  

def dashboard():
    user = User.query.first()
    return render_template('dashboard.html',user=user)

@app.route('/show_all')
def show_all():
   user = User.query.first()
   return render_template('show_all.html', user=user,users = User.query.all() )

@app.route('/update',methods=['GET','POST'])
def update():
    user = User.query.first()
    form = RegisterForm()
    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        user.password=form.password.data
        db.session.commit()
        return render_template('dashboard.html',user=user) 
    return render_template('update.html',form=form,user=user) 
            
@app.route('/profile')
def profile():
    user = User.query.first()
    return render_template('profile.html',user=user) 
if __name__ =='__main__' :
    app.run(debug=True)    

  