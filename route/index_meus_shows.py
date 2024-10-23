from flask import redirect, render_template, Blueprint, url_for, session
from DAO.token_verificacao import verificar_integridade_token, verificar_session
from DAO.meus_shows_request import meus_shows_request()
from database.database import db, Shows

index_meus_shows = Blueprint('index_meus_shows', __name__)

@index_meus_shows.route('/index/meus/shows', methods = ['GET'])
def index_meus_shows_generator():
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
    
        meus_shows = meus_shows_request()

        return render_template('')

    except Exception as ex:
        print(f'Erro104 {ex}')
        return redirect(url_for('login.login_generator'))