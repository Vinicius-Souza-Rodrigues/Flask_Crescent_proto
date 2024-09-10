from flask import Blueprint, render_template, request, redirect, url_for, session

register_user = Blueprint('register_user', __name__)

@register_user.route('/register_user', method = ['GET'])
def register_user_generator():
    return render_template('register_user.html')

@register_user.route('/register_user', method = ['POST'])
def register_user_form():

    return redirect(url_for('route.index_generator'))