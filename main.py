from flask import Blueprint, render_template, url_for

main = Blueprint('Main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/perfil')
def profile():
    return render_template('perfil.html')

@main.route('/termos')
def terms():
    return render_template('termos.html')

@main.route('/politicas')
def polices():
    return render_template('politicas.html')