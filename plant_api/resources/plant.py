from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with
from plant_api.app import session
from ming import collection, schema, Field
from util import bson_wrapper

Plant = collection(
    'plants', session,
    Field('_id', schema.ObjectId),
    Field('common_name', str)
)

parser = reqparse.RequestParser()
parser.add_argument('arg', type=int)

class PlantEndpoint(restful.Resource):
    def get(self, plant_id):
        p = Plant({'common_name': 'Fotp'})
        p.m.save()
        print Plant.m.find({}).all()
        return {'fads': 'bar'}



