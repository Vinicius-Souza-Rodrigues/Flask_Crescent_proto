from flask import Flask, redirect, render_template, Blueprint, url_for, request

login = Blueprint('login', __name__)

@login.route('/', methods = ['GET'])
def login_generator():
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def login_form():
    email = request.form.get('email')
    senha = request.form.get('password')

    

    return redirect(url_for('index_generator'))
    