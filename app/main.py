"""
Optei por fazer a API em python pois estou mais familiarizado com a linguagem, e tambem para praticar mais 
com a FastAPI, por se tratar de uma aplicacao web    .

Este modulo define a estrutura principal da aplicacao FastAPI. Ele instancia a aplicacao,
configura as rotas (endpoints) e integra as operações de CRUD para as entidades `Produto` e `Categoria`.

Logica geral:
- Utiliza FastAPI para criar uma API RESTful com documentação automatica (Swagger UI).
- Adota o padrao de separacao de camadas: `crud` para logica de negocio, `schemas` para validacao e estrutura dos dados, `models` para o mapeamento das tabelas no banco, e `database` para configuração do SQLite.
- A injecao de dependencia e feita com `Depends(get_db)` para garantir o gerenciamento automatico da sessao com o banco.
- O `Base.metadata.create_all` garante que as tabelas sejam criadas com base nos modelos declarados, caso ainda nao existam.
- Cada rota da API chama diretamente a funcao correspondente em `crud`, mantendo o codigo limpo e desacoplado.

Endpoints disponiveis:
- Produtos:
    GET     /produtos            → Lista todos os produtos
    GET     /produtos/{id}       → Busca produto por ID
    POST    /produtos            → Cria novo produto
    PUT     /produtos/{id}       → Atualiza produto
    DELETE  /produtos/{id}       → Remove produto
- Categorias:
    POST    /categorias          → Cria nova categoria
    GET     /categorias          → Lista todas as categorias
- Teste de vida:
    GET     /ping                → Retorna {"msg": "pong"} para verificar se a API está ativa
"""

from fastapi import FastAPI, Depends # aqui usei depends para simular a injecao de um sessao do db
from fastapi import HTTPException # para ajudar a identificacao de erros e execucoes
from .config import settings 
from app import crud
from app.database import get_db # alinhada ao Depends para fazer a injecao
from app.database import Base, engine #  modelagem de tabelas e conexao com o db
from app.schemas.product import Produto, CriarProduto, AtualizarProduto
from app.schemas.categoria import CriarCategoria, Categoria
from app.models.product import ProdutoModel
from sqlalchemy.orm import Session # interacao com o banco
from typing import List # retorno de endpoints como lista de objetos

# cria todas as tabelas
Base.metadata.create_all(bind=engine)

# instancia da fastapi 
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

# endpoint GET /produtos
@app.get("/produtos")
def listar_produtos():
    return crud.listar_produtos()
    
# endpoit GET /produtos{id}
@app.get("/produtos/{id}")
def id_produtos(id: int):
   return crud.id_produtos(id)

# endpoint POST /produtos
@app.post("/produtos") 
def criar_produto(produto: CriarProduto):
    return crud.criar_produto(produto)
            
# endpoint PUT /produtos/{id}
@app.put("/produtos/{id}")
def atualizar_produtos(id: int, produto_atualizado: AtualizarProduto):
    return crud.atualizar_produtos(id, produto_atualizado)
        
# endpoint DEL /produto/{id}
@app.delete("/produtos/{id}")
def excluir_produto(id: int):
    return crud.excluir_produto(id)

# endpoint POST/categoria
@app.post("/categorias", response_model=Categoria, status_code=201)
def nova_categoria(categoria: CriarCategoria, db: Session = Depends(get_db)):
    return crud.criar_categoria(db, categoria)

# endpoint GET /categorias
@app.get("/categorias", response_model=List[Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.listar_categorias(db)

# teste funcionamento da api
@app.get("/ping")
async def ping():
    return {"msg": "pong"}