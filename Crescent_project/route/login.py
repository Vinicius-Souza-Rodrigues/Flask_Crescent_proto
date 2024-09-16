from flask import Flask, redirect, render_template, Blueprint, url_for, session

login = Blueprint('login', __name__)

@login.route('/', methods = ['GET'])
def login_generator():
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def login_form():
    
    return redirect(url_for('index_generator'))
    