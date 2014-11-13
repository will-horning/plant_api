import pytest

@pytest.fixture(scope='module')
def plant_api_app():
    return plant_api.create_app()

from test_search import *
from test_bed import *
from test_plant import *
from test_user import *
from test_geo import *
