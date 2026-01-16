from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Carregando o arquivo config.py
app.config.from_object(Config)

# Inicializando o objeto do Banco de Dados
db = SQLAlchemy(app)

# Importando as rotas
# from routes import *   # Este arquivo será criado depois.

@app.route('/')
def index():
    return "O servidor está rodando e o banco de dados está configurado!"

if __name__ == '__main__':
    # Cria o banco de dados se não existir
    with app.app_context():
        db.create_all()

    # Roda o servidor
    app.run(debug=True)
    