from subprocess import check_output
from flask import Flask
from flask.ext.assets import Environment, Bundle
from webassets.filter import Filter, register_filter

class CoffeeifyFilter(Filter):
    name = 'coffeeify'

    def input(self, _in, out, **kwargs):
        path = kwargs['source_path']
        out.write(check_output(['browserify', '-t', 'coffeeify', path]))

    def output(self, _in, out, **kwargs):
        out.write(_in.read())

register_filter(CoffeeifyFilter)

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    assets = Environment(app)
    js = Bundle('coffee/main.coffee', filters=['coffeeify'], output='main.js')
    assets.register('js_all', js)
    from views import api_blueprint
    app.register_blueprint(api_blueprint)
    return app