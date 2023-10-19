# Prompt de Comando ==============================================
# python -m venv env_agendaweb - Criar o ambiente virtual
# .\env_agendaweb\Scripts\activate - Ativar o ambiente virtual
# pip install flask - Instalar o flask
# flask --app agendaweb run --debug - Iniciar o servidor do Flask
# pip freeze > requirements.txt - Lista das ferramentas utilizadas
# pip install mysql-connector-python
# ================================================================

import mysql.connector
from flask import Flask, render_template, request

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'agenda'
)

cursor = conexao.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/processar', methods=['POST'])
def processar():
    texto = request.form['texto']
    return f'Texto digitado: {texto}'

if __name__ == '__main__':
    app.run()