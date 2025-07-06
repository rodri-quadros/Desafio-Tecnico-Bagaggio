"""
Este modulo centraliza as configuracoes da aplicacao. Define a classe Settings, que utiliza pydantic_settings.BaseSettings para carregar automaticamente variaveis de ambiente e configurar a aplicacao com base em boas praticas.

 As principais configuracoes incluem:
 - PROJECT_NAME: nome do projeto exibido no Swagger.
 - BASE_DIR: diretorio base do projeto (dinamico).
 - SQLITE_DB_PATH: caminho absoluto para o banco SQLite.
 - DEBUG: ativa/desativa modo de desenvolvimento.
 - API_VERSION: versão atual da API (usada nos endpoints).
 - env_file: define o uso de um arquivo .env para variaveis externas.

A instancia 'settings' no final do arquivo pode ser importada em qualquer parte do projeto para acessar essas configuracoes de forma segura e centralizada.
"""

import os
from typing import ClassVar
from pydantic_settings import BaseSettings # lib que cria o ambiente env dentro da classe automaticamente usando a validacao do proprio pydantic

# config db
class Settings(BaseSettings):
    PROJECT_NAME: str = "Desafio Bagaggio"
    BASE_DIR: ClassVar [str] = os.path.dirname(os.path.abspath(__file__)) 
    SQLITE_DB_PATH: str =  f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}" # f string para dinamizar a alocacao
    DEBUG: bool = True # apesar de opcional, escolhi colocar o DEBUG para simular o codigo em um ambiente de desenvolvimento real
    API_VERSION: str = "v1"
    class Config:
        env_file = ".env"
settings = Settings()

