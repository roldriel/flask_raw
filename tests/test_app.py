import pytest
from src.app import create_app  # Asumiendo que el archivo se llama app.py y está en src/

@pytest.fixture
def client():
    app = create_app()  # Crear la app usando el factory
    app.config['TESTING'] = True  # Activar modo de pruebas
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!!' in response.data  # O cualquier contenido esperado
