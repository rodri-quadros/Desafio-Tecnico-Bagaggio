from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ProdutoModel(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    categoria_id = Column(Integer,ForeignKey("categorias.id"), nullable=False)
    categoria = relationship("CategoriaModel", back_populates="produtos")