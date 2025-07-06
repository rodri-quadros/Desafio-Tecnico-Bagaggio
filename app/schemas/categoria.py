"""
Esse modulo define os esquemas (schemas) utilizados para a entidade Categoria,
usando o Pydantic para validacao e serializacao de dados.

As classes aqui definidas representam diferentes momentos do ciclo de vida de uma categoria:
- CategoriaBase: estrutura básica com o campo obrigatorio 'nome'.
- CriarCategoria: herda de CategoriaBase e é usada na criacao de uma nova categoria (POST).
- Categoria: representa o modelo completo retornado pela API, incluindo o 'id' da categoria.

A classe interna Config com `orm_mode = True` permite que objetos ORM (como os retornados
pelo SQLAlchemy) sejam convertidos diretamente para esses esquemas.

Esses esquemas sao utilizados para garantir a integridade e clareza na troca de dados entre
as camadas da aplicacao e os endpoints definidos no FastAPI.
"""

from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nome: str

class CriarCategoria(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        orm_mode = True
