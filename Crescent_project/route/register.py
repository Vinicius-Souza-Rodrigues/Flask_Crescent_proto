from flask import Flask, redirect, render_template, Blueprint, url_for, session

register = Blueprint('register', __name__)

@register.route('/options_register' method = ['GET'])
def options_register():
    return

@register.route('/register', method = ['GET'])
def register_user_generator():
    return render_template('register.html')

@register.route('/register', method = ['GET'])
def register_admin_generator():
    return render_template('register.html')

@register.route('/register', method = ['GET'])
def register_imprensa_generator():
    return render_template('register.html')

@register.route('/register', method = ['GET'])
def register_patrocinador_generator():
    return render_template('register.html')    

@register.route('/register_admin', method = ['POST'])
def register_adm_form():
    pass

@register.route('/register_patrocinador', method = ['POST'])
def register_patrocinador_form():
    return 'algo'

@register.route('/register_imprensa', method = ['POST'])
def register_imprensa_form():

@register.route('/register_user', method = ['POST'])
def register_form():
