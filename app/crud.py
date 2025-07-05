from fastapi import HTTPException
from typing import List
from app.schemas.product import Produto, CriarProduto, AtualizarProduto

produtos = []
contador_id = 1

def gerar_id_automaticamente():
    global contador_id
    novo_id = contador_id
    contador_id += 1
    return novo_id


# endpoint GET /produtos
def listar_produtos():
    if not produtos:
        return{"aviso": "Nenhum produto foi cadastrado ainda"}
    return produtos
    
# endpoit GET /produtos{id}
def id_produtos(id: int):
    for p in produtos:  #################################################################################
        if p.id == id:  # percorre por todos os produtos para checar se ele existe e retornar o id dele # 
            return p    #################################################################################
    raise HTTPException(status_code=404, detail="Produto não encontrado") # caso nao exista, sera exibido um erro

# endpoint POST /produtos
def criar_produto(produto: CriarProduto):
    novo_id = gerar_id_automaticamente()
    for i in produtos:
        if i.nome == produto.nome:
            raise HTTPException(status_code=409, detail=f"Produto: {produto.id} duplicado")
    novo_produto = Produto(
        id=novo_id,
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        quantidade=produto.quantidade
    )
    produtos.append(novo_produto)
    return novo_produto
            
# endpoint PUT /produtos/{id}
def atualizar_produtos(id: int, produto_atualizado: AtualizarProduto):
    for i in produtos:
        if i.id == id:
            if produto_atualizado.nome is not None:
                i.nome = produto_atualizado.nome
            if produto_atualizado.descricao is not None:
                i.descricao = produto_atualizado.descricao
            if produto_atualizado.preco is not None:
                i.preco = produto_atualizado.preco
            if produto_atualizado.quantidade is not None:
                i.quantidade = produto_atualizado.quantidade
            return i
    raise HTTPException(status_code=404, detail=f"{id} não encontrado")
        
# endpoint DEL /produto/{id}
def excluir_produto(id: int):
    for i in produtos:
        if i.id == id:
            produtos.remove(i)
            return {
                "mensagem":f"Produto {id} removido",
                "produtos": produtos
                }
    raise HTTPException(status_code=400, detail="Produto não encontrado")