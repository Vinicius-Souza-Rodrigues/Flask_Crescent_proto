from flask import redirect, render_template, Blueprint, url_for, session
from DAO.token_verificacao import verificar_session, verificar_integridade_token 

index_user_config = Blueprint('index_user_config', __name__)

@index_user_config.route('/index/user/configuração')
def index_user_config_generator():
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
    

    except Exception as ex:
        print(f'erro13 {ex}')

    return render_template('index_user_config.html') 