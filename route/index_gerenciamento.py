from flask import redirect, render_template, Blueprint, url_for, request
from database.database import db, Shows
import os

index_gerenciamento = Blueprint('index_gerenciamento', __name__)

@index_gerenciamento.route('/index/gerenciamento', methods = ['GET'])
def index_gerenciamento_generator():
    return render_template('index_main_gerenciamento.html')

@index_gerenciamento.route('/index/gerenciamento', methods=['POST'])
def index_gerenciamento_form():
    name = request.form.get('title')
    local = request.form.get('local')
    descricao = request.form.get('description')
    preco = request.form.get('preco')
    img_file = request.files.get('url_img')
    
    filename = img_file.filename
    static_caminho = os.path.join(os.getcwd(), 'static', 'uploads')
    url_img = os.path.join(static_caminho, filename)
    img_file.save(url_img)

    novo_show = Shows(
        title=name,
        local=local,
        description=descricao,
        preco=preco,
        url_img=url_img
    )

    db.session.add(novo_show)
    db.session.commit()
    
    return redirect(url_for('index_gerenciamento.index_gerenciamento_generator'))