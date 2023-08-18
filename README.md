# Projeto Flask: Lista de Jogos com CRUD

Este é um projeto Flask que implementa uma lista de jogos com operações de CRUD (Criar, Ler, Atualizar e Deletar). O projeto permite que você adicione, edite, exclua e visualize jogos na lista.

## Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy
- MySQL Server

## Configuração

1. Clone este repositório para sua máquina local:

```sh
git clone https://github.com/leocalheiros/jogoteca.git
```

2.Instale as dependências:
```
pip install -r requirements.txt
```

3.Configure o banco de dados na máquina:
```
Importe o banco de dados chamado 'jogoteca' como exemplo ou crie um banco de dados com "CREATE DATABASE jogoteca" e execute o arquivo "criartabelasnobanco_opcional.py" para criar as tabelas.
Abra o arquivo config.py e atualize a configuração SQLALCHEMY_DATABASE_URI para corresponder às suas configurações do MySQL.
Os usuários cadastrados nesse banco de dados são:
nick: lzn / senha: 123
nick: mila / senha: 1234

```


## Executando o projeto:
```
python jogoteca.py
O aplicativo será executado em http://127.0.0.1:5000/.
```

## Funcionalidades:
```
Acesse a página inicial para ver a lista de jogos.
Faça login para adicionar, editar ou excluir jogos.
Os jogos são exibidos em uma tabela com suas informações.
Clique no botão "Editar" para editar um jogo existente.
Clique no botão "Deletar" para excluir um jogo existente.
Clique no botão "Novo Jogo" para adicionar um novo jogo à lista.
Clique no botão "Logout" para realizar o logout na página.
Consulta dos usuários e jogos via API
```

## Endpoints da API
- **GET api/jogos: consulta todos os jogos cadastrados juntamente com suas características
- **GET api/usuarios: consulta todos os usuários cadastrados 

## Vídeo de usabilidade:
https://github.com/leocalheiros/jogoteca/assets/123272507/c6f9264a-4e99-4949-8e32-a75944c2d756
