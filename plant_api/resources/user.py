from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class User(restful.Resource):
    def get(self, user_id):
        return {
            'type': 'user',
            'id': user_id,
            'arg': parser.parse_args()['arg']
        }
