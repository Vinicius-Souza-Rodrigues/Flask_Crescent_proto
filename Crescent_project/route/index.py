from flask import Flask, redirect, render_template, Blueprint, url_for, session

index = Blueprint('index', __name__)

@index.route('/index/usuario', methods = ['GET'])
def index_usuario_generator():
    token = session['token']
    id = session['id_user']

    if not token or id:
        return redirect(url_for('login.login_generator'))
    
    

    return render_template('index_main_usuario.html')

@index.route('/index/gerenciamento', methods = ['GET'])
def index_gerenciamento_generator():
    return render_template('index_main_gerenciamento.html')