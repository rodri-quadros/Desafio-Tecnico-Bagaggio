from fastapi import HTTPException
from typing import List
from app.schemas.product import Produto
from app.models.product import ProdutoModel
from app.schemas.categoria import CriarCategoria
from app.models.categoria import CategoriaModels
from app.database import SessionLocal
from sqlalchemy.orm import Session

produtos = []
contador_id = 1

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def gerar_id_automaticamente():
    global contador_id
    novo_id = contador_id
    contador_id += 1
    return novo_id


# endpoint GET /produtos
def listar_produtos():
    db = SessionLocal()
    produtos = db.query(ProdutoModel).all()
    db.close()
    if not produtos:
        return{"aviso": "Nenhum produto foi cadastrado ainda"}
    return produtos
    
# endpoit GET /produtos{id}
def id_produtos(id: int):
    db = SessionLocal()
    produto = db.query(ProdutoModel).filter(ProdutoModel.id == id).first()
    db.close()
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado") # caso nao exista, sera exibido um erro
    return produto

# endpoint POST /produtos
def criar_produto(produto: Produto):
    db = SessionLocal()
    produto_existente = db.query(ProdutoModel).filter(ProdutoModel.nome == produto.nome).first()
    if produto_existente:
        db.close()
        raise HTTPException(status_code=409, detail=f"Produto com nome '{produto.nome}' já existe na base")
    novo_produto = ProdutoModel(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        quantidade=produto.quantidade
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    db.close()
    return novo_produto
            
# endpoint PUT /produtos/{id}
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
    
        
# endpoint DEL /produto/{id}
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
   
def criar_categoria(db: Session, categoria: CriarCategoria):
    nova_categoria = CategoriaModels(nome=categoria.nome)
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria

def listar_categorias(db: Session):
    return db.query(CategoriaModels).all()
