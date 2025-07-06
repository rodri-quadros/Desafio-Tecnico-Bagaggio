"""
Esse modulo define o modelo de dados `ProdutoModel`, responsável por mapear a entidade Produto para a tabela `produtos` no banco de dados.

A classe herda de `Base`, permitindo a criacao automatica da tabela e seus campos conforme definidos.

O modelo estabelece um relacionamento de chave estrangeira com a entidade Categoria (tabela `categorias`), refletindo a ligacao entre produtos e suas respectivas categorias.

Decisoes de design:
- Todos os campos sao marcados como `nullable=False` para reforcar a integridade e obrigatoriedade dos dados.
- Foi utilizada a estratégia de relacionamento via `relationship()` para acesso direto ao objeto `CategoriaModels`, facilitando consultas relacionais no SQLAlchemy.
- O campo `index=True` no `id` otimiza buscas por ID, comum em endpoints REST.

Esse modelo e utilizado diretamente pelo SQLAlchemy para manipulacao persistente dos dados, sendo o espelho da estrutura de produtos em operacoes de CRUD.
"""


from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.categoria import CategoriaModels

class ProdutoModel(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False) # decidi atribuir a FK para tornar o id obrigatorio
    categoria = relationship(CategoriaModels, back_populates="produtos")