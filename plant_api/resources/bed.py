from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class Bed(restful.Resource):
    def get(self, bed_id):
        return {
            'type': 'bed',
            'id': bed_id,
            'arg': parser.parse_args()['arg']
        }
