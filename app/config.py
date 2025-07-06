import os
from typing import ClassVar
from pydantic_settings import BaseSettings # lib que cria o ambiente env dentro da classe automaticamente

# config db
class Settings(BaseSettings):
    PROJECT_NAME: str = "Desafio Bagaggio"
    BASE_DIR: ClassVar [str] = os.path.dirname(os.path.abspath(__file__))
    SQLITE_DB_PATH: str =  f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}" # f string para dinamizar a alocacao
    print(SQLITE_DB_PATH)

    DEBUG: bool = True # apesar de opcional, escolhi colocar o DEBUG para simular o codigo em um ambiente de desenvolvimento
    API_VERSION: str = "v1"
    class Config:
        env_file = ".env"
settings = Settings()

