import requests
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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
