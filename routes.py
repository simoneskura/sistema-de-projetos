from flask import render_template, redirect, url_for, flash, request
from app import app
from db import db
from models import User, Project, Subitem
from forms import UserForm, ProjectForm, SubitemForm
from sqlalchemy.exc import IntegrityError

# Página inicial
@app.route('/')
def index():
    projetos = Project.query.all()
    return render_template('index.html', projetos=projetos)

# Cadastro de usuário
@app.route('/usuarios/novo', methods=['GET', 'POST'])
def novo_usuario():
    form = UserForm()
    if form.validate_on_submit():
        cpf_limpo = "".join(filter(str.isdigit, form.cpf.data))
        
        usuario = User(
            nome=form.nome.data,
            cpf=cpf_limpo,
            email=form.email.data,
            telefone=form.telefone.data,
            data_nascimento=form.data_nascimento.data,
            aceite=form.aceite.data
        )
        
        try:
            db.session.add(usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!')
            return redirect(url_for('listar_usuarios'))
        except IntegrityError:
            db.session.rollback()
            flash('Erro: O e-mail ou CPF informado  já está cadastrado no sistema, tente novamente.', 'danger')
            return render_template('cadastro_usuario.html', form=form)
            
    return render_template('cadastro_usuario.html', form=form)

# Listar usuários
@app.route('/usuarios')
def listar_usuarios():
    usuarios = User.query.all()
    return render_template('lista_usuario.html', usuarios=usuarios)

# Remover usuário
@app.route('/usuarios/deletar/<int:id>', methods=['POST'])
def deletar_usuario(id):
    usuario = User.query.get_or_404(id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        flash(f'O usuário {usuario.nome} e todos os seus projetos foram removidos.')
    except Exception:
        db.session.rollback()
        flash('Erro ao tentar excluir o usuário. Tente novamente.', 'danger')
    return redirect(url_for('listar_usuarios'))

# Adicionar projeto
@app.route('/projetos/novo', methods=['GET', 'POST'])
def novo_projeto():
    # Verifica se existem usuários antes de abrir o formulário
    usuarios_existentes = User.query.all()
    if not usuarios_existentes:
        flash('Você precisa cadastrar pelo menos um usuário para ser o dono do projeto.')
        return redirect(url_for('novo_usuario'))

    form = ProjectForm()
    # Preenche a lista de donos com os usuários cadastrados
    form.dono.choices = [(u.id, u.nome) for u in User.query.order_by('nome')]
    
    if form.validate_on_submit():
        projeto = Project(
            nome=form.nome.data,
            descricao=form.descricao.data,
            data_inicio=form.data_inicio.data,
            data_fim=form.data_fim.data,
            user_id=form.dono.data
        )
        db.session.add(projeto)
        db.session.commit()
        flash('Projeto criado com sucesso!')
        return redirect(url_for('index'))
    return render_template('cria_projeto.html', form=form)

# Detalhes do projeto
@app.route('/projeto/<int:id>', methods=['GET', 'POST'])
def detalhe_projeto(id):
    projeto = Project.query.get_or_404(id)
    form = SubitemForm()
    # Preenche a lista de responsáveis com os usuários cadastrados
    form.responsavel.choices = [(u.id, u.nome) for u in User.query.all()]
    
    if form.validate_on_submit():
        tarefa = Subitem(
            titulo=form.titulo.data,
            descricao=form.descricao.data,
            status=form.status.data,
            prazo=form.prazo.data,
            project_id=projeto.id,
            user_id=form.responsavel.data
        )
        db.session.add(tarefa)
        db.session.commit()
        flash('Tarefa adicionada!')
        return redirect(url_for('detalhe_projeto', id=projeto.id))
    
    # Lista de participantes
    participantes = set([t.responsavel for t in projeto.subitens])
    return render_template('detalhes_projeto.html', projeto=projeto, form=form, participantes=participantes)

# Apagar projeto
@app.route('/projeto/deletar/<int:id>', methods=['POST'])
def deletar_projeto(id):
    projeto = Project.query.get_or_404(id)
    try:
        db.session.delete(projeto) 
        db.session.commit()
        flash('O projeto e suas tarefas foram excluídos.')
    except Exception:
        db.session.rollback()
        flash('Erro ao tentar excluir o projeto.', 'danger')
    return redirect(url_for('index'))

# Remover tarefa
@app.route('/tarefa/deletar/<int:id>', methods=['POST'])
def deletar_tarefa(id):
    tarefa = Subitem.query.get_or_404(id)
    projeto_id = tarefa.project_id
    db.session.delete(tarefa)
    db.session.commit()
    flash('A tarefa foi  excluída!')
    return redirect(url_for('detalhe_projeto', id=projeto_id))

# Resumo do Usuário
@app.route('/usuario/<int:id>/resumo')
def resumo_usuario(id):
    usuario = User.query.get_or_404(id)
    return render_template('resumo_usuario.html', usuario=usuario)