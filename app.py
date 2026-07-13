from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/vagas')
def vagas():
    return render_template('vagas.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')