import pytest
from plant_api.app import create_app

@pytest.fixture(scope='module')
def plant_api_app():
    return create_app({'TESTING': True})

from test_plant import *
# from test_search import *
# from test_bed import *
# from test_user import *
# from test_geo import *
