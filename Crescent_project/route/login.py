from flask import Flask, redirect, render_template, Blueprint, url_for, session

login = Blueprint('login', __name__)

@login.route('/', method = ['GET'])
def login_generator():
    return render_template('login.html')

@login.route('/', method = ['POST'])
def login_form():
    email = session.get('email')
    password = session.get('password')
