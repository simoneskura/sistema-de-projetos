from db import db

#Tabela de usuários
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    aceite = db.Column(db.Boolean, default=False)

    # Relacionamentos
    # 'projetos_criados' acessa os objetos que um usuário é dono
    projetos_criados = db.relationship('Project', backref='dono', lazy=True, cascade="all, delete-orphan")
    # 'tarefas_atribuidas' acessa os subitens em que um  usuário é responsável
    tarefas_atribuidas = db.relationship('Subitem', backref='responsavel', lazy=True, cascade="all, delete-orphan") 

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)

# Chave estrangeira que relaciona  o Dono do Projeto ao usuário
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relacionamento com Subitens, se um projeto é excluído, as tarefas também serão.
    subitens = db.relationship('Subitem', backref='projeto', lazy=True, cascade="all, delete-orphan")

class Subitem(db.Model):
    __tablename__ = 'subitems'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pendente') # Pendente, Em andamento, Concluído
    prazo = db.Column(db.Date, nullable=True)

    # chaves estrangeiras
    # Identifica a qual projeto uma tarefa pertence
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    # Usuário que é  responsávelpor uma tarefa 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
