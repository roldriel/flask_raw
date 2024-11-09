import pytest
from src.app import create_app

@pytest.fixture
def client():
    """Client test function"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!!' in response.data
