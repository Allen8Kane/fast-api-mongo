from bson.objectid import ObjectId
from fastapi import APIRouter
from dataclasses import make_dataclass
from pymongo import MongoClient
from src.models.user import User
from src.services.user import User_service
from src.utils.PyObjectId import PyObjectId


router = APIRouter()
service = User_service()

# /api/users
@router.get("/")
async def get_users(skip: int = 0, limit: int = 10):
    user = service.get_users(skip, limit)
    return user

@router.get("/{user_id}")
async def get_user(user_id: PyObjectId):
    user = service.get_user(user_id)
    return user

@router.post("/")
async def create_user(user: User):
    _user = service.create_user(user)
    _user['_id'] = str(_user['_id'])
    return _user

@router.put("/{user_id}")
async def update_user(user_id: PyObjectId, user: User):
    print(user_id)
    print(user)
    user = service.update_user(user_id, user)
    return user

@router.delete("/{user_id}")
async def delete_user(user_id: PyObjectId):
    user = service.delete_user(user_id)
    return user
