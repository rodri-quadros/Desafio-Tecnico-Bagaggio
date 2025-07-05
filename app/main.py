from fastapi import FastAPI
from fastapi import HTTPException
from .config import settings
from app import crud
from app.schemas.product import Produto, CriarProduto, AtualizarProduto

# conexao framework
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
@app.post("/produtos") #status 201 para gerar status "created" como boa pratica
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

@app.get("/ping")
async def ping():
    return {"msg": "pong"}