from flask import redirect, render_template, Blueprint, url_for, request, session

index_user_config = Blueprint('index_user_config', __name__)

@index_user_config.route('/index/user/configuração')
def index_user_config_generator():
    return render_template('index_user_config.html') 