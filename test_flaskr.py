import pytest
from flaskr import create_app
from models import setup_db

@pytest.fixture
def client():
    app = create_app()
    db = setup_db(app)
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.data == b'Hello, World!'
    assert rv.status_code == 200
