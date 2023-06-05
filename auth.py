from flask import Blueprint, render_template, url_for

auth = Blueprint('Auth',__name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'Esta é a página de logout!'

