import pymongo, os
from flask import Flask
from flask.ext.pymongo import PyMongo
mongo = PyMongo()


def create_app(config={}):
    app = Flask(__name__)
    app.config.update(config)
    app.config['MONGO_URI'] = os.environ['MONGOLAB_TEST_URI'] 
    mongo.init_app(app)
    from assets import assets
    assets.init_app(app)
    from views import api_blueprint
    app.register_blueprint(api_blueprint)
    return app

