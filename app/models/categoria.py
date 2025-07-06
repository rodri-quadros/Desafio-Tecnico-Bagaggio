"""
Esse modulo define o modelo ORM para a entidade `Categoria`, que representa
as categorias as quais os produtos pertencem no sistema.

A classe `CategoriaModels` herda de `Base`, sendo mapeada para a tabela `categorias`
no banco de dados SQLite. Essa estrutura permite criar e manipular registros
de categorias com SQLAlchemy, utilizando os recursos de relacionamento com a entidade `Produto`.

Campos definidos:
- `id`         → Identificador unico da categoria (chave primária).
- `nome`       → Nome da categoria (unico e obrigatorio).
- `produtos`   → Relacionamento bidirecional com a entidade Produto.

Esse relacionamento e estabelecido via `relationship`, permitindo navegacao entre
categorias e os produtos relacionados.
"""

from app.database import Base
from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import relationship

class CategoriaModels(Base):
    __tablename__="categorias" # define o nome da nova tabela
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    produtos = relationship("ProdutoModel", back_populates="categoria") # conecta com outros modulos com o campo categoria