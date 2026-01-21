Gerenciador de Projetos e Tarefas

Esta Aplicação web foi desenvolvida em Python e Flask para gerenciamento de
usuários, projetos e tarefas. Nesse sentido, este sistema permite cadastrar,
visualizar e excluir informações, mantendo a organização e segurança dos dados.

Tecnologias Utilizadas

- Python 3;
- Flask;
- Flask-SQLAlchemy
- Flask-WTF;
- SQLite.
- HTML, CSS e JavaScript.

Como Rodar o Projeto

1. Clone o repositório:
git clone https://github.com/simoneskura/sistema-de-projetos/
2. Acesse a pasta do projeto.
3. Crie e ative um ambiente virtual:
py -3 -m venv .venv
.venv\Scripts\activate

4. Instale as dependências:
pip install -r requirements.txt

5. Execute o sistema:
python app.py
6. No navegador, acesse o seguinte:
http://127.0.0.1:5000

Principais rotas

- /usuarios/novo: cadastrar novo usuário;
- /usuarios: lista os usuários cadastrados;
- /usuario/<id>/resumo: resumo do usuário, projetos e tarefas.
- /projetos/novo: criar novo projeto
- /projeto/<id>: detalhes do projeto e gerenciamento de tarefas.

Decisões Técnicas

- Durante o desenvolvimento, implementei aspectos relacionados a acessibilidade
para usuários que utilizam leitores de tela. Utilizei html semântico, ARIA
labels, navegação por teclado e gerenciamento de foco.
- O banco de dados foi criado automaticamente na primeira execução. Além disso,
Quando o modelo era alterado, o banco era reiniciado para manter a
estrutura.
-No backend, , utilizei o validador de e-mail do Flask-WTF e a biblioteca
validate-docbr para validar o CPF.
- No frontend, criei máscaras  de entrada para CPF e Telefone, utilizando o
JavaScript.
- A estrutura do projeto foi separada por responsabilidades (config, models,
forms, routes e templates), para facilitar a manutenção do código.

Melhorias futuras

- Implementação de edição de usuários, projetos e tarefas.
- Implementar login e  autenticação.
- Envio de Notificações por e-mail para os responsáveis pelas tarefas.

Observação: utilizei a inteligência artificial para me ajudar a criar as
máscaras de validação do telefone e do CPF e para auxiliar com o CSS pelo fato
de ter aspectos visuais.

