from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with
from plant_api import mongo
from util import bson_wrapper

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class Plant(restful.Resource):
    @bson_wrapper
    def get(self, plant_id):
        return mongo.db.plants.find_one_or_404({'_id': plant_id})




