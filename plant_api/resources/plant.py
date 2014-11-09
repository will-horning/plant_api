from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class Plant(restful.Resource):
    def get(self, plant_id):
        return {
            'type': 'plant',
            'id': plant_id,
            'arg': parser.parse_args()['arg']
        }




