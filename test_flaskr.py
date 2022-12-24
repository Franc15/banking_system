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

'''
    Test for registration functionality. User is expected to pass in personal details and the 
    endpoint should return a json with the user's details and a success message
'''
def test_registration(client):
    rv = client.post('/register', json={
        "fname": "Francis",
        "lname": "Kikulwe",
        "gender": "male",
        "dob": "1998-09-11",
        "phone": "0712345678",
        "email": "francis@gmail.com",
        "country": "Tanzania",
        "password": "password",
        "empStat": "employed"

    })
    assert rv.status_code == 200
    assert rv.json['success'] == True
    assert rv.json['data']['fname'] == "Francis"
    assert rv.json['data']['lname'] == "Kikulwe"


