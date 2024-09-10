from flask import Flask, redirect, render_template, Blueprint, url_for, session

register_option = Blueprint('register_option', __name__)

@register_option.route('/options_register', method = ['GET'])
def options_register():
    return render_template('options_register.html')
