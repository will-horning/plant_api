import plant_api, pytest, json
from .test_main import plant_api_app

def test_plant(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/1')
        assert json.loads(response.data)['id'] == 1

def test_plants(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/')
        assert type(json.loads(response.data)) == list
