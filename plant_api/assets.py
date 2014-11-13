from flask.ext.assets import Environment, Bundle
from subprocess import check_output
from webassets.filter import Filter, register_filter

class CoffeeifyFilter(Filter):
    name = 'coffeeify'

    def input(self, _in, out, **kwargs):
        path = kwargs['source_path']
        out.write(check_output(['browserify', '-t', 'coffeeify', path]))

    def output(self, _in, out, **kwargs):
        out.write(_in.read())

register_filter(CoffeeifyFilter)

js = Bundle('coffee/main.coffee', filters=['coffeeify'], output='main.js')
assets = Environment()
assets.register('js_all', js)
