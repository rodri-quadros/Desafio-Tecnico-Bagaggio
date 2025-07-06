# 🧰 API de Produtos – Desafio Bagaggio

Este projeto implementa uma **API RESTful** com operações de **CRUD** para gerenciamento de produtos e categorias, desenvolvido com **FastAPI**, banco de dados **SQLite**, testes automatizados com **Pytest** e conteinerização via **Docker**.

## 📁 Estrutura de Pastas
desafio_bagaggio/
├── app/
│ ├── init.py
│ ├── config.py # Configurações do projeto (nome, versão, path do banco, debug)
│ ├── crud.py # Regras de negócio para produtos e categorias
│ ├── database.py # Conexão com SQLite + função de sessão
│ ├── main.py # Endpoints da API com FastAPI
│ ├── models/
│ │ ├── init.py
│ │ ├── product.py # Modelo ORM de Produto
│ │ └── categoria.py # Modelo ORM de Categoria
│ └── schemas/
│ ├── init.py
│ ├── product.py # Schemas Pydantic de Produto (validação)
│ └── categoria.py # Schemas Pydantic de Categoria
├── tests/
│ └── products_test.py # Testes automatizados com TestClient do FastAPI
├── Dockerfile # Dockerfile para build da imagem da aplicação
├── docker-compose.yml # Compose com FastAPI e bind da porta
├── requirements.txt # Dependências da aplicação
└── README.md # Este arquivo

## 💡 Lógica Principal

A aplicação foi estruturada com separação clara entre camadas:

- **Modelos ORM** com SQLAlchemy para mapear as tabelas `produtos` e `categorias`
- **Schemas Pydantic** para validação de entrada/saída dos dados nos endpoints
- **Camada de CRUD** com toda a lógica de negócio: criação, busca, atualização e remoção
- **Endpoints com FastAPI** para cada operação (GET, POST, PUT, DELETE)
- **Conexão com banco** centralizada em `database.py`, com função `get_db()` para injeção de dependência
- **Testes automatizados** cobrindo as principais funcionalidades

---

## 🧪 Endpoints RESTful

- `GET /produtos`: listar todos os produtos
- `GET /produtos/{id}`: buscar produto por ID
- `POST /produtos`: criar novo produto
- `PUT /produtos/{id}`: atualizar produto existente
- `DELETE /produtos/{id}`: deletar produto
- `GET /categorias`: listar categorias
- `POST /categorias`: criar nova categoria

---

## ⚙️ Tecnologias Utilizadas e Justificativas

- **Python**: Linguagem de fácil leitura, ampla adoção em APIs, compatível com FastAPI e SQLAlchemy.
- **FastAPI**: Framework moderno, rápido e eficiente para criação de APIs, com documentação automática via Swagger UI.
- **SQLite**: Banco leve, ideal para desafios técnicos locais e persistência simples sem servidor de banco.
- **Docker**: Permite empacotar a aplicação e rodar em qualquer ambiente com um único comando, garantindo portabilidade.
- **Pytest**: Ferramenta robusta para testes unitários e integração.

---

## 🐳 Como rodar com Docker

### 1. Clonar o repositório
```bash
git clone (https://github.com/rodri-quadros/Desafio-Tecnico-Bagaggio.git)
cd Desafio-Tecnico-Bagaggio
```
### 2. Build da imagem Docker
```bash
docker build -t bagaggio-api .
```
### 3. Rodar a aplicação
```bash
docker run -d -p 8000:8000 bagaggio-api
```
Acesse no navegador: http://localhost:8000/docs para usar a interface Swagger.

---

# 🧪 Testes Automatizados
Execute os testes com:
```bash
docker run --rm bagaggio-api pytest
```
Ou, localmente (fora do Docker):
```bash
pip install -r requirements.txt
pytest
```

---

## 🌍 Deploy em produção

A aplicação foi publicada gratuitamente via [Railway](https://railway.app):

🔗 Acesse o Swagger UI: (https://desafio-tecnico-bagaggio-production.up.railway.app/docs)  
🔗 Acesse a Redoc: (https://desafio-tecnico-bagaggio-production.up.railway.app/redoc)

---

# 📅 Linha do Tempo do Desenvolvimento

  📁 Estruturação do projeto com FastAPI 
  
  🧱 Criação dos modelos e schemas 
  
  🛠️ Implementação dos endpoints RESTful 
  
  💾 Persistência com SQLite e SQLAlchemy 
  
  🔁 Refatoração e modularização completa 
  
  🧪 Criação e validação dos testes automatizados
  
  🐳 Conteinerização com Docker (Dockerfile + Compose) 

  🌍 Deploy simulando ambiente de produção
  
  📚 Comentários explicativos e organização por boas práticas 
  
  📄 Documentação README.md finalizada 

---

# 👨‍💻 Autor
Rodrigo Quadros
Estudante de Ciência da Computação – Universidade Veiga de Almeida
Email: rodrigoquadros.dev@gmail.com

