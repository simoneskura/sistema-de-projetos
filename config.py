import os

# O base directory ajuda o Python a encontrar a pasta do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Classe que tem as configurações do projeto

    # A SECRET_KEY é utilizada para proteger os formulários contra ataques
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7a00289cdc2288f382af0efd70f628c5'

    #habilita mensagens de erro
    DEBUG = True

    # Garante que os formulários tenham proteção  CSRF
    WTF_CSRF_ENABLED = True

    # Limita a quantidade de itens por página
    ITEMS_PER_PAGE = 10
    
    # Define onde o arquivo do banco de dados SQLite será criado
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Desativa um recurso do SQLAlchemy que consome bastante memória
    SQLALCHEMY_TRACK_MODIFICATIONS = False