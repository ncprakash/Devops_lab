import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING']=true
    with app.test.client() as client:
        yield client

def test_home_page(client):
    respones=client.get('/')
    assert respones.status_code==200
    print("home page tested")

def test_students_api(client):
    respones=client.get('/students')
    assert respones.status_code==200
    data =respones.get_json()
    assert data['status']=='success'
    assert data['count'] ==3
    print("student api is test passed")

def test_health_check(client):
    response=client.get('/health')
    assert respones.status_code==200
    data=respones.get_json()
    print("test passed")
    