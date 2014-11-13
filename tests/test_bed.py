import plant_api, pytest, json
from .test_main import plant_api_app


def test_bed(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/beds/1')
        assert json.loads(response.data)['id'] == 1

def test_beds(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/beds/')
        assert type(json.loads(response.data)) == list
