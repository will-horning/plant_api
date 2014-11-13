import plant_api, pytest, json
from .test_main import plant_api_app

def test_geo(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/geo/1')
        assert json.loads(response.data)['id'] == 1

