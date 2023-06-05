from flask import Blueprint, render_template, url_for, request, redirect

auth = Blueprint('Auth',__name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')


# O que vier por POST, o padrão é GET
@auth.route('/signup', methods=['POST'])
def signup_post():
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    endereco = request.form.get('endereco')
    numero = request.form.get('numero')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    cep = request.form.get('cep')
    concordo = request.form.get('concordo')

    print(nome, email, senha, estado, concordo)

    return redirect(url_for('Auth.login'))


@auth.route('/login')
def login():
    return render_template('login.html')


# O que vier por POST, o padrão é GET
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    senha = request.form.get('senha')

    print(email, senha)

    return redirect(url_for('Main.profile'))

@auth.route('/logout')
def logout():
    return 'Esta é a página de logout!'

