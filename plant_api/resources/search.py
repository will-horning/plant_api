from flask.ext import restful
from flask.ext.restful import reqparse
from util import bson_wrapper

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class Search(restful.Resource):
    @bson_wrapper
    def get(self, search_id):
        return mongo.db.users.find_one_or_404({'_id': search_id})