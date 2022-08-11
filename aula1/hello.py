from flask import Flask, render_template
app = Flask("aula1")

@app.route('/')
def hello_world():

    nome="Vinicius Gabriel"

    produtos = [
        {"Nome": "Livro", "Preco": 200},
        {"Nome": "Playstation", "Preco": 2000.50}
    ]

    return render_template("index.html", nome=nome, aProdutos=produtos), 200

app.run()