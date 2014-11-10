import plant_api, pytest, json

@pytest.fixture(scope='module')
def plant_api_app():
    return plant_api.create_app()

def test_plant(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/1')
        assert json.loads(response.data)['id'] == 1

def test_plants(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/')
        assert type(json.loads(response.data)) == list
