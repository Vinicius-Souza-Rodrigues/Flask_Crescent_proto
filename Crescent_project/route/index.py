from flask import Flask, redirect, render_template, Blueprint, url_for, session
from DAO.token_verificacao import verificar_session, verificar_integridade_token
from DAO.shows_request import shows_request

index = Blueprint('index', __name__)

@index.route('/index/usuario', methods = ['GET'])
def index_usuario_generator():
    token = session['token']
    id = session['id_user']

    if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
        return redirect(url_for('login.login_generator'))
    
    shows = shows_request()
    print(shows)

    return render_template('index_main_usuario.html', shows=shows)

@index.route('/index/gerenciamento', methods = ['GET'])
def index_gerenciamento_generator():
    return render_template('index_main_gerenciamento.html')