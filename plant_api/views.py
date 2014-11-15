from flask import render_template, Blueprint, current_app
from flask.ext import restful
from resources import PlantEndpoint

api_blueprint = Blueprint('api', __name__)

api = restful.Api(api_blueprint)
api.add_resource(PlantEndpoint, '/plants/<int:plant_id>')

@api_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
