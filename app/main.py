from fastapi import FastAPI
from .config import settings
from typing import List
from pydantic import BaseModel

# conexao framework
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade: int

produtos: List[Produto] = []

# endpoint GET /produtos
@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/ping")
async def ping():
    return {"msg": "pong"}