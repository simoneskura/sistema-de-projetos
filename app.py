from flask import Flask
from config import Config
from db import db

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Carregando as configurações
app.config.from_object(Config)

# Inicializando o Banco de Dados
db.init_app(app)

# Importando as rotas e criando as tabelas
with app.app_context():
    
    # Importando todas as rotas do arquivo routes.py
    from routes import *

    # Cria o arquivo app.db com as tabelas se ele ainda não existir
    db.create_all()

if __name__ == '__main__':
    # Roda o servidor em modo de desenvolvimento
    app.run(debug=True)