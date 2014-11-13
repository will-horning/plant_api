from flask.ext import restful
from flask.ext.restful import reqparse
from plant_api import mongo
from util import bson_wrapper

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class User(restful.Resource):
    @bson_wrapper
    def get(self, user_id):
        return mongo.db.users.find_one_or_404({'_id': user_id})