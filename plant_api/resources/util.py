from json import loads
from bson.json_util import dumps

def bson_wrapper(f):
    def wrapper(*args, **kwargs):
        document = loads(dumps(f(*args, **kwargs)))
        del document['_id']
        return document
    return wrapper
