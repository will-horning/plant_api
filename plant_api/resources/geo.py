from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class Geo(restful.Resource):
    def get(self, geo_id):
        return {
            'type': 'geo',
            'id': geo_id,
            'arg': parser.parse_args()['arg']
        }
