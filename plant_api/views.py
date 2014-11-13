import requests
from flask import render_template, Blueprint, current_app
from flask.ext import restful
from resources import Bed, Plant, Geo, Search, User
from plant_api import mongo

api_blueprint = Blueprint('api', __name__)

api = restful.Api(api_blueprint)
api.add_resource(Bed, '/beds/<int:bed_id>')
api.add_resource(Plant, '/plants/<int:plant_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Search, '/search/<int:search_id>')
api.add_resource(Geo, '/geo/<int:geo_id>')

@api_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
