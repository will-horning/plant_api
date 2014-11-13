import pymongo, os
from subprocess import check_output
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.assets import Environment, Bundle
from webassets.filter import Filter, register_filter

mongo = PyMongo()

class CoffeeifyFilter(Filter):
    name = 'coffeeify'

    def input(self, _in, out, **kwargs):
        path = kwargs['source_path']
        out.write(check_output(['browserify', '-t', 'coffeeify', path]))

    def output(self, _in, out, **kwargs):
        out.write(_in.read())
register_filter(CoffeeifyFilter)

def create_app(config={}):
    app = Flask(__name__)
    app.config.update(config)
    app.config['MONGO_URI'] = os.environ['MONGOLAB_TEST_URI'] 
    mongo.init_app(app)
    assets = Environment(app)
    js = Bundle('coffee/main.coffee', filters=['coffeeify'], output='main.js')
    assets.register('js_all', js)
    from views import api_blueprint
    app.register_blueprint(api_blueprint)
    return app