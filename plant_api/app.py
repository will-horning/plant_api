from flask import Flask
from ming import Session, create_datastore
from assets import assets

session = Session()
from views import api_blueprint

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    session.bind = create_datastore(app.config['MONGO_URI'])
    assets.init_app(app)
    app.register_blueprint(api_blueprint)
    return app

