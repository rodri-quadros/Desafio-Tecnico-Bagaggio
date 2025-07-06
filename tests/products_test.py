"""
Esse modulo contem os testes automatizados para os endpoints da API de Produtos.

Os testes sao realizados com o `TestClient` da FastAPI, simulando requisicoes HTTP aos endpoints implementados no backend da aplicação.

Cada teste verifica um comportamento essencial da API:
- Criacao de categorias para uso nos produtos (com nome unico utilizando `uuid4`)
- Criacao de produtos com dados detalhados e esperados no modelo
- Listagem de todos os produtos registrados
- Busca de um produto por ID
- Atualizacao dos dados de um produto especifico
- Exclusao de produto e verificacao da remocao

O uso de `uuid4()` garante unicidade nos nomes, evitando conflitos em testes repetidos.

Todos os testes seguem o padrão de:
1. Preparação de dados
2. Chamada do endpoint
3. Verificacao da resposta (status code e conteudo)

Esses testes garantem que a API esteja funcionando corretamente conforme os requisitos do desafio.
"""

from fastapi.testclient import TestClient
from app.main import app
from uuid import uuid4

# gera o cliente teste
client = TestClient(app)

def criar_categoria_padrao():
    nome_unico = f"Categoria-{uuid4()}" 
    categoria = {"nome": nome_unico}
    response = client.post("/categorias", json=categoria)
    assert response.status_code == 201
    return response.json()["id"]

def test_criar_produto():
    categoria_id = criar_categoria_padrao()
    nome_unico = f"Mochila-{uuid4()}"
    response = client.post("/produtos", json={
        "nome": nome_unico,
        "descricao": "Mochila com compartimento acolchoado para notebook até 17'', ideal para modelos com 16GB RAM. Possui porta USB externa, design moderno, alças reforçadas e material resistente à água.",
        "preco": 289.90,
        "quantidade": 5,
        "categoria_id": categoria_id
    })
    assert response.status_code == 200 or response.status_code == 201
    assert "id" in response.json()

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list) or isinstance(response.json(), dict)

def test_buscar_produto_por_id():
    categoria_id = criar_categoria_padrao()
    produto = {
        "nome": f"Bolsa-{uuid4()}",
        "descricao": "Bolsa compacta com alça ajustável e compartimento acolchoado ideal para smartphones de até 7''. Possui zíper antifurto, tecido impermeável e espaço interno para documentos e cartões.",
        "preco": 99.90,
        "quantidade": 10,
        "categoria_id": categoria_id
    }
    post_resp = client.post("/produtos", json=produto)
    assert post_resp.status_code == 200 or post_resp.status_code == 201
    produto_criado = post_resp.json()
    get_resp = client.get(f"/produtos/{produto_criado['id']}")
    assert get_resp.status_code == 200
    assert get_resp.json()["nome"] == produto["nome"]

def test_atualizar_produto():
    categoria_id = criar_categoria_padrao()
    produto = {
        "nome": f"Case-{uuid4()}",
        "descricao": "Case rígido",
        "preco": 99.90,
        "quantidade": 25,
        "categoria_id": categoria_id
    }
    post_resp = client.post("/produtos", json=produto)
    id_produto = post_resp.json()["id"]
    atualizado = {
        "nome": "Case Compacto para Acessórios Tech",
        "descricao": "Case rígido com divisórias internas para transporte seguro de mouse sem fio, carregadores, cabos e pequenos eletrônicos. Fecho em zíper duplo, alça de mão e revestimento interno acolchoado.",
        "preco": 149.90,
        "quantidade": 30,
        "categoria_id": categoria_id
    }
    put_resp = client.put(f"/produtos/{id_produto}", json=atualizado)
    assert put_resp.status_code == 200
    assert put_resp.json()["nome"] == "Case Compacto para Acessórios Tech"

def test_excluir_produto():
    categoria_id = criar_categoria_padrao()
    produto = {
        "nome": f"Case-{uuid4()}",
        "descricao": "Case resistente com revestimento interno em EVA moldado, ideal para teclados mecânicos até 40cm. Fechamento em zíper, alça de transporte e estrutura semi-rígida com proteção contra impactos.",
        "preco": 299.90,
        "quantidade": 15,
        "categoria_id": categoria_id
    }
    post_resp = client.post("/produtos", json=produto)
    id_produto = post_resp.json()["id"]
    del_resp = client.delete(f"/produtos/{id_produto}")
    assert del_resp.status_code == 200
    assert del_resp.json()["detail"] == "Produto excluído com sucesso"
    get_resp = client.get(f"/produtos/{id_produto}") # verifica se a exclusao foi feita corretamente
    assert get_resp.status_code == 404
