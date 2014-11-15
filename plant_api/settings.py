import os

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    MONGO_URI = os.environ['MONGOLAB_URI']

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    MONGO_URI = os.environ['MONGOLAB_TEST_URI']

class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    MONGO_URI = 'mim://plant_api'