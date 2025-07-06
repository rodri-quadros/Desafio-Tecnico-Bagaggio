from app.database import Base
from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import relationship

class CategoriaModels(Base):
    __tablename__="categorias"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    produtos = relationship("ProdutoModel", back_populates="categoria")





    