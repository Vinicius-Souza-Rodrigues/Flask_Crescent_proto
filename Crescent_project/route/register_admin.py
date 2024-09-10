from flask import Flask, redirect, render_template, Blueprint, url_for, session

register_admin = Blueprint('register_admin', __name__)

@register_admin.route('/register_admin', method = ['GET'])
def register_admin_generator():
    return render_template('register_admin.html')

@register_admin.route('/register_admin', method = ['POST'])
def register_admin_form():
    
    return redirect(url_for('aaa'))