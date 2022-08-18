# coding: utf-8
from flask import Flask, redirect, render_template, request, session, url_for
app = Flask("aula2")

#Criando uma chave de criptografia
app.secret_key = "Aula de flask 2_testes"

@app.route('/')
def hello_world():

    #criação de variavel
    nome="Vinicius Gabriel"

    produtos = [
        {"Nome": "Livro", "Preco": 200},
        {"Nome": "Playstation", "Preco": 2000.50}
    ]

    return render_template("index.html", nome=nome, aProdutos=produtos), 200


#Nova rota de teste
@app.route("/teste")
def funcao_teste(variavel = "Vinicius"):#passando uma variavel
    return "Nova rota teste <br> Variável: {}".format(variavel), 200


# Rota formulário
@app.route("/form")
def form():
    return render_template("form.html"), 200


# Rota tratamento do formulário
@app.route("/form_recebe", methods=["GET", "POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamar direto no GET", 200


# Rota form de login
@app.route("/login")
def login():
    return render_template("login.html"), 200 


#Rota para validar o formulário
@app.route("/login_validar", methods=["POST"])
def login_validar():
    if request.form["usuario"] == "vinicius" and request.form["senha"] == "12345":
        session["usuario"] = request.form["usuario"] 
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))   
    
    else:
        return "Usuario/senha inválidos, digite novamente.", 200


#Rota para a área restrita
@app.route("/restrito")
def acesso_restrito():
    if session["codigo"] == 1:
        return "Bem-Vindo a area restrita!! <br> Usuário: {} <br>Código: {}".format(session["usuario"],session["codigo"]), 200
    else:
        return "Acesso Inválido", 200

app.run()