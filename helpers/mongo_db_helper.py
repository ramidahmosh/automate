import pymongo
import pytest
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient(pytest.config_file.get("system","db_host"), int(pytest.config_file.get("system","db_port")))
db = client.doctrine_odm
users = db.users

# example of get data from mongodb
def get_user_last_name(userid):
    user_id_obj = {"_id": ObjectId(userid)}
    last_name = pymongo.collection.Collection.distinct(users, "last_name", user_id_obj)
    return last_name