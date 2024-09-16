from flask import Flask, redirect, render_template, Blueprint, url_for, session

register_prop = Blueprint('register_prop', __name__)

@register_prop.route('/register_prop', methods = ['GET'])
def register_prop_generator():

    return render_template('register_prop.html')