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


app = Flask(__name__)

assets = Environment(app)

# api = restful.Api(app)
# api.add_resource(Page, '/pages/<int:page_id>')

js = Bundle('coffee/main.coffee', filters=['coffeeify'], output='main.js')
assets.register('js_all', js)

import plant_api.views