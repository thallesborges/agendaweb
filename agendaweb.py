# Prompt de Comando ==============================================
# python -m venv env_agendaweb - Criar o ambiente virtual
# .\env_agendaweb\Scripts\activate - Ativar o ambiente virtual
# pip install flask - Instalar o flask
# flask --app agendaweb run --debug - Iniciar o servidor do Flask
# pip install gunicorn - Instalar o gunicorn (Procfile)
# pip freeze > requirements.txt - Lista das ferramentas utilizadas
# ================================================================


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<user>')
def user(user):
    return render_template("users.html", user = user)

if __name__ == '__main__':
    app.run()