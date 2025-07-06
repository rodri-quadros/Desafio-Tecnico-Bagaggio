from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.categoria import Categoria

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade: int
    categoria: Categoria

class CriarProduto(BaseModel):
    nome: str
    descricao: str
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)
    categoria_id: int
    class Config():
        orm_mode = True
        

class AtualizarProduto(BaseModel):
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float] = Field(gt=0)
    quantidade: Optional[int] = Field(ge=0)

