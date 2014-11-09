import plant_api, pytest, json

@pytest.fixture(scope='module')
def plant_api_app():
    return plant_api.create_app()

def test_index(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/users/55?arg=55')
        assert json.loads(response.data)['arg'] == 55
