from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class Search(restful.Resource):
    def get(self, search_id):
        return {
            'type': 'search',
            'id': search_id,
            'arg': parser.parse_args()['arg']
        }
