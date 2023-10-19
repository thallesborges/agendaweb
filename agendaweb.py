import mysql.connector
from flask import Flask, render_template, request

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'agenda'
)

cursor = conexao.cursor()

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
    #sql_credencial = f'SELECT 1 FROM USUARIO WHERE NOME = {usuario} AND SENHA = {senha}'
    #cursor.execute(sql_credencial)
    #result_sql_credencial = cursor.fetchall()
    #print(result_sql_credencial)
    print(f'{usuario} e {senha}')
    return render_template("index.html")


@app.route('/homepage')
def recuperar():
    return render_template("homepage.html")

if __name__ == '__main__':
    app.run()

# SELECT 1 FROM USUARIO WHERE NOME = {nome} AND SENHA = {senha}; 