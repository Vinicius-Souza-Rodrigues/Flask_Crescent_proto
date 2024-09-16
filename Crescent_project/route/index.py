from flask import Flask, redirect, render_template, Blueprint, url_for, session

index = Blueprint('index', __name__)

@index.route('/index', methods = ['GET'])
def index_generator():
    return render_template('index_base1.html')

@index.route('/index/admin', methods = ['GET'])
def index_admin_generator():
    return render_template('index_base2.html')