import plant_api, pytest, json


@pytest.fixture(scope='module')
def plant_api_app():
    return plant_api.create_app()


def test_plant(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/1')
        assert json.loads(response.data)['id'] == 1

def test_user(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/users/1')
        assert json.loads(response.data)['id'] == 1

def test_search(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/search/1')
        assert json.loads(response.data)['id'] == 1

def test_geo(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/geo/1')
        assert json.loads(response.data)['id'] == 1

def test_bed(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/beds/1')
        assert json.loads(response.data)['id'] == 1

def test_plants(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/plants/')
        assert type(json.loads(response.data)) == list

def test_users(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/users/')
        assert type(json.loads(response.data)) == list

def test_beds(plant_api_app):
    with plant_api_app.test_client() as client:
        response = client.get('/beds/')
        assert type(json.loads(response.data)) == list
