"""
Este modulo implementa as funções de lógica de negócio da aplicacao,
manipulando os dados da entidade Produto e Categoria com base nos modelos ORM.

A conexão com o banco de dados e feita por meio de sessoes SQLAlchemy (`SessionLocal`).
Cada funcao cuida de abrir, utilizar e fechar a sessão conforme necessario.

As funcionalidades aqui implementadas se conectam diretamente com os endpoints definidos em main.py:

- listar_produtos()           → GET /produtos
- id_produtos(id)            → GET /produtos/{id}
- criar_produto(produto)     → POST /produtos
- atualizar_produtos(id, produto) → PUT /produtos/{id}
- excluir_produto(id)        → DELETE /produtos/{id}
- criar_categoria() e listar_categorias() tratam a entidade auxiliar Categoria

Todos os retornos e exceções seguem os padrões do FastAPI e HTTP, garantindo boas práticas de resposta a API.
"""

from fastapi import HTTPException
from typing import List
from app.schemas.product import Produto
from app.models.product import ProdutoModel
from app.schemas.categoria import CriarCategoria
from app.models.categoria import CategoriaModels
from app.database import SessionLocal
from sqlalchemy.orm import Session

# gera a conexao com o db usada em todas as funcoes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# conecta -> endpoint GET /produtos
def listar_produtos():
    db = SessionLocal()
    produtos = db.query(ProdutoModel).all()
    db.close()
    if not produtos:
        return{"aviso": "Nenhum produto foi cadastrado ainda"}
    return produtos
    
# conecta -> endpoit GET /produtos{id}
def id_produtos(id: int):
    db = SessionLocal()
    produto = db.query(ProdutoModel).filter(ProdutoModel.id == id).first()
    db.close()
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado") # caso nao exista, sera exibido um erro
    return produto

# conecta -> endpoint POST /produtos
def criar_produto(produto: Produto):
    db = SessionLocal()
    produto_existente = db.query(ProdutoModel).filter(ProdutoModel.nome == produto.nome).first()
    if produto_existente:
        db.close()
        raise HTTPException(status_code=409, detail=f"Produto com nome '{produto.nome}' já existe na base")
    novo_produto = ProdutoModel(            #############################################
        nome=produto.nome,                  #                                           #
        descricao=produto.descricao,        # De acordo com o schema, faz as instancias # 
        preco=produto.preco,                # do novo protudo                           #
        quantidade=produto.quantidade,      #                                           # 
        categoria_id=produto.categoria_id   #                                           #
    )                                       #############################################
    db.add(novo_produto) # adiciona o novo produto ao db
    db.commit() # confirma a adicao
    db.refresh(novo_produto) # atualiza o db com os novos dados
    db.close()
    return novo_produto
            
# conecta -> endpoint PUT /produtos/{id}
def atualizar_produtos(id: int, produto_atualizado: Produto):
    db = SessionLocal()
    produto = db.query(ProdutoModel).filter(ProdutoModel.id == id).first()
    if produto is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"{id} não encontrado")
    if produto_atualizado.nome is not None:
        produto.nome = produto_atualizado.nome
    if produto_atualizado.descricao is not None:
        produto.descricao = produto_atualizado.descricao
    if produto_atualizado.preco is not None:
        produto.preco = produto_atualizado.preco
    if produto_atualizado.quantidade is not None:
        produto.quantidade = produto_atualizado.quantidade
    db.commit()
    db.refresh(produto)
    db.close()
    return produto
    
        
# conecta -> endpoint DEL /produto/{id}
def excluir_produto(id: int):
    db = SessionLocal()
    produto = db.query(ProdutoModel).filter(ProdutoModel.id == id).first()
    if produto is None:
        db.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
    db.close()
    return {"detail":"Produto excluído com sucesso"}

# conecta ->    
def criar_categoria(db: Session, categoria: CriarCategoria):
    nova_categoria = CategoriaModels(nome=categoria.nome)
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria

# conecta -> 
def listar_categorias(db: Session):
    return db.query(CategoriaModels).all()
