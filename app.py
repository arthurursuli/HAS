from flask import Flask, render_template
from flask import request

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

@app.route('/cursos', methods=["GET", "POST"])
def cursos():
    quantidade = 3

    if request.method == "POST":
        quantidade = 9

    return render_template("cursos.html", quantidade=quantidade)

@app.route('/vagas', methods=["GET", "POST"])
def vagas():
    quantidade = 3

    if request.method == "POST":
        quantidade = 9

    return render_template("vagas.html", quantidade=quantidade)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')