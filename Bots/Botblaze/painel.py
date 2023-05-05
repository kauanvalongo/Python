from flask import Flask, render_template, jsonify
from scraper import pegar_dados, total, gerar_numero_aleatorio, perdas_blaze


app = Flask(__name__, static_folder='static')

@app.route("/")
def homepage():
    dados = pegar_dados()
    pegar_total = total()
    perdas = perdas_blaze()
    numero = gerar_numero_aleatorio()
    return render_template("home.html", dados=dados, pegar_total=pegar_total, numero=numero, perdas=perdas)

@app.route('/atualizar_dados')
def atualizar_dados():
    # Atualize os dados com os valores atualizados
    dados = pegar_dados()  # Função fictícia para obter os dados atualizados
    return jsonify({'dados': dados})


@app.route('/perdas_atualizar')
def perdas_atualizar():
    perdas = perdas_blaze()

    return jsonify({'perdas': perdas})




@app.route('/gerar_numero')
def gerar_numero():
    # Atualize os dados com os valores atualizados
    numero = gerar_numero_aleatorio()  # Função fictícia para obter os dados atualizados
    return jsonify({'numero': numero})


@app.route('/atualizar_total')
def atualizar_total():
    pegar_total = total()  # Atualize a variável pegar_total com o valor atualizado
    return jsonify({'pegar_total': pegar_total})


if __name__ == "__main__":
    app.run(debug=True)
