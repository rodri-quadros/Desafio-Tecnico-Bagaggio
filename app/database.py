"""
Esse modulo configura a conexao com o banco de dados SQLite usando SQLAlchemy.
Define a engine, a base declarativa para os modelos ORM, e uma fabrica de sessoes.
Tambem inclui a funcao `get_db`, que fornece uma sessao de banco para as rotas da API.
Essa funcao e usada com Depends no FastAPI para garantir o fechamento correto da sessao.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, Session
from app.config import Settings

SQLITE_DB_PATH = "sqlite:///./datanase.db" 
engine = create_engine(SQLITE_DB_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# define a conexao com o db
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()