from fastapi.testclient import TestClient
from app.main import app
from uuid import uuid4

client = TestClient(app)

def test_criar_produto():
    nome_unico = f"Notebook-{uuid4()}"
    response = client.post("/produtos", json={
        "nome": nome_unico,
        "descricao": "Notebook com 16GB RAM",
        "preco": 3499.90,
        "quantidade": 5
    })
    assert response.status_code == 200 or response.status_code == 201
    assert "id" in response.json()

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_produto_por_id():
    produto = {
        "nome": f"Smartphone-{uuid4()}",
        "descricao": "Celular com 128GB",
        "preco": 1999.90,
        "quantidade": 10
    }
    post_resp = client.post("/produtos", json=produto)
    assert post_resp.status_code == 200 or post_resp.status_code == 201

    produto_criado = post_resp.json()
    get_resp = client.get(f"/produtos/{produto_criado['id']}")
    assert get_resp.status_code == 200
    assert get_resp.json()["nome"] == produto["nome"]

def test_atualizar_produto():
    produto = {
        "nome": "Mouse",
        "descricao": "Mouse sem fio",
        "preco": 99.90,
        "quantidade": 25
    }
    post_resp = client.post("/produtos", json=produto)
    id_produto = post_resp.json()["id"]

    atualizado = {
        "nome": "Mouse Gamer",
        "descricao": "Mouse RGB",
        "preco": 149.90,
        "quantidade": 30
    }
    put_resp = client.put(f"/produtos/{id_produto}", json=atualizado)
    assert put_resp.status_code == 200
    assert put_resp.json()["nome"] == "Mouse Gamer"

def test_excluir_produto():
    produto = {
        "nome": "Teclado",
        "descricao": "Teclado mecânico",
        "preco": 299.90,
        "quantidade": 15
    }
    post_resp = client.post("/produtos", json=produto)
    id_produto = post_resp.json()["id"]
    del_resp = client.delete(f"/produtos/{id_produto}")
    assert del_resp.status_code == 200
    assert del_resp.json()["detail"] == "Produto excluído com sucesso"
    get_resp = client.get(f"/produtos/{id_produto}")
    assert get_resp.status_code == 404
