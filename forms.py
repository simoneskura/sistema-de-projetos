from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from validate_docbr import CPF
from datetime import date

# Cadastro de usuário
class UserForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired(message="O nome é um campo obrigatório.")])

        # O validador Email() verifica se existe o símbolo @ e um domínio válido
    email = StringField('E-mail', validators=[DataRequired(), Email(message="E-mail inválido.")])
    cpf = StringField('CPF', validators=[DataRequired(message="O CPF é um campo obrigatório.")])
    telefone = StringField('Telefone', validators=[DataRequired(message="O telefone é um campo obrigatório.")])
    data_nascimento = DateField('Data de Nascimento', format='%Y-%m-%d', validators=[DataRequired()])

    # O cadastro só é feito se  o aceite estiver marcado
    aceite = BooleanField('Aceito os termos de cadastro', validators=[DataRequired(message="É necessário aceitar os termos.")])
    submit = SubmitField('Cadastrar Usuário')

# Valida o CPF usando a biblioteca validate-docbr
    def validate_cpf(self, field):
        # Remove caracteres não numéricos
        cpf_limpo = "".join(filter(str.isdigit, field.data))
        validator = CPF()
        if not validator.validate(cpf_limpo):
            raise ValidationError('CPF inválido. Verifique os números e tente novamente.')

        # Garante que a data de nascimento não seja no futuro.
    def validate_data_nascimento(self, field):
        if field.data > date.today():
            raise ValidationError('A data de nascimento não pode ser uma data futura.')

# Formulário para criação de projetos
class ProjectForm(FlaskForm):
    nome = StringField('Nome do Projeto', validators=[DataRequired()])
    descricao = TextAreaField('Descrição do projeto', validators=[DataRequired()])
    data_inicio = DateField('Data de Início', format='%Y-%m-%d', validators=[DataRequired()])
    data_fim = DateField('Data de Fim', format='%Y-%m-%d', validators=[DataRequired()])
    dono = SelectField('Dono do Projeto', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Criar Projeto')

#Valida para que o projeto não comece em data passada.
    def validate_data_inicio(self, field):
        if field.data < date.today():
            raise ValidationError('O projeto não pode começar em uma data que já passou.')

#  A data de término deve ser maior ou igual a data de início.
    def validate_data_fim(self, field):
        if field.data < self.data_inicio.data:
            raise ValidationError('A data de fim não pode ser anterior à data de início.')

# Formulário para as tarefas do projeto
class SubitemForm(FlaskForm):
    titulo = StringField('Título do Subitem', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
        # Status do projeto
    status = SelectField('Status', choices=[
        ('Pendente', 'Pendente'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído')
    ], validators=[DataRequired()])
    prazo = DateField('Prazo (Opcional)', format='%Y-%m-%d', validators=[])
    responsavel = SelectField('Responsável pela Tarefa', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Adicionar tarefa')

#Garante que o prazo da tarefa não seja uma data que já passou. 
    def validate_prazo(self, field):
        if field.data and field.data < date.today():
            raise ValidationError('O prazo não pode ser uma data passada.')