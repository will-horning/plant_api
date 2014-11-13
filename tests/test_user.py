import plant_api, pytest, json
from .test_main import plant_api_app

def test_user(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/users/1')
        assert json.loads(response.data)['id'] == 1

def test_users(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/users/')
        assert type(json.loads(response.data)) == list
