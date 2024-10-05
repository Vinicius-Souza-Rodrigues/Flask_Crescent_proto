from flask import redirect, render_template, Blueprint, url_for, request
from database.database import db, Shows

index_gerenciamento = Blueprint('index_gerenciamento', __name__)

@index_gerenciamento.route('/index/gerenciamento', methods = ['GET'])
def index_gerenciamento_generator():
    return render_template('index_main_gerenciamento.html')

@index_gerenciamento.route('/index/gerenciamento', methods = ['POST'])
def index_gerenciamento_form():
    name = request.form.get('title')
    local = request.form.get('local')
    descricao = request.form.get('description')
    preco = request.form.get('preco')

    novo_show = Shows(
        title = name,
        local = local,
        description = descricao,
        preco = preco
    )

    db.session.add(novo_show)
    db.session.commit()
    
    return redirect(url_for('index_gerenciamento.index_gerenciamento_generator'))