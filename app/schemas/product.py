"""
Este modulo define os schemas utilizados pela API para a entidade Produto,
incluindo validacoes, restricoes e estrutura de entrada/saida de dados.

Utiliza a biblioteca Pydantic (`BaseModel`, `Field`) para garantir tipagem estatica,
validacao automatica e integração com o ORM (via `orm_mode`), facilitando a comunicação entre
as camadas da aplicacao.

Sao definidos tres schemas distintos:

- Produto: representa o modelo completo de um produto, incluindo a categoria aninhada.
  Usado como resposta padrao da API nos metodos de leitura (GET).
- CriarProduto: define os campos necessários para a criacao de um novo produto.
  Aplica validacoes especificas como preco > 0 e quantidade ≥ 0.
- AtualizarProduto: permite atualizacoes parciais com todos os campos opcionais.
  Tambem aplica restricoes de integridade nos campos preenchidos.

O relacionamento com a categoria e feito por meio do campo `categoria`
e `categoria_id`, promovendo separação entre entrada e saida.

Esses schemas sao utilizados diretamente nos endpoints definidos em `main.py` e manipulados pelas funcoes do modulo `crud.py`.
"""

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
    preco: float = Field(gt=0) # nao permitir valores menores que 0
    quantidade: int = Field(ge=0) # permitir valores maiores ou iguais a 0
    categoria_id: int
    class Config():
        orm_mode = True
        

class AtualizarProduto(BaseModel):
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float] = Field(gt=0)
    quantidade: Optional[int] = Field(ge=0)
    categoria_id: Optional[int]
