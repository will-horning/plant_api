import requests
<<<<<<< HEAD
from flask import render_template, Blueprint
from flask.ext import restful
from resources import Bed, Plant, Geo, Search, User

api_blueprint = Blueprint('api', __name__)
=======
from flask import render_template
from flask.ext import restful
from plant_api import app
from resources import Bed, Plant, Geo, Search, User

api = restful.Api(app)

api.add_resource(Bed, '/beds/<int:bed_id>')
api.add_resource(Plant, '/plants/<int:plant_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Search, '/search/<int:search_id>')
api.add_resource(Geo, '/geo/<int:geo_id>')
>>>>>>> a147ede1273df4997b8aea8aff88af4f42fa840f

api = restful.Api(api_blueprint)
api.add_resource(Bed, '/beds/<int:bed_id>')
api.add_resource(Plant, '/plants/<int:plant_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Search, '/search/<int:search_id>')
api.add_resource(Geo, '/geo/<int:geo_id>')

@api_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
