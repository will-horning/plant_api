import plant_api, pytest, json

@pytest.fixture(scope='module')
def plant_api_app():
    return plant_api.create_app()

def test_plant(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/55?arg=55')
        assert json.loads(response.data)['arg'] == 55

def test_user(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/users/55?arg=55')
        assert json.loads(response.data)['arg'] == 55

def test_search(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/search/55?arg=55')
        assert json.loads(response.data)['arg'] == 55

def test_geo(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/geo/55?arg=55')
        assert json.loads(response.data)['arg'] == 55

def test_bed(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/beds/55?arg=55')
        assert json.loads(response.data)['arg'] == 55
