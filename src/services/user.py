from pydantic.types import Json
from pymongo import MongoClient
from src.models.user import User
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from src.utils.PyObjectId import PyObjectId

MONGO_URL = os.getenv('MONGO_URL')

class User_service:
    _db_users = MongoClient(MONGO_URL)['users']
    
    def create_user(self, user: User):
        user_dict = dict(user.__dict__)
        user_id = self._db_users.insert_one(user_dict).inserted_id
        _user = self._db_users.find_one(user_id)
        return _user
    
    def update_user(self, user_id: PyObjectId, user: User):
        user_dict = dict(user.__dict__)
        self._db_users.update_one({'_id': ObjectId(user_id)},{'$set': user_dict})
        _user = self._db_users.find_one(ObjectId(user_id))
        _user['_id'] = str(_user['_id'])
        return _user
        
    def get_users(self, skip: int, limit: int):
        users = []
        for user in self._db_users.find().skip(skip).limit(limit):
            user['_id'] = str(user['_id'])
            users.append(user)
        return users
    
    def get_user(self, user_id: ObjectId):
        user = self._db_users.find_one(ObjectId(user_id))
        user['_id'] = str(user['_id'])
        return user

    
    def delete_user(self, user_id: str):
        user = self._db_users.find_one_and_delete({'_id': ObjectId(user_id)})
        return user
    