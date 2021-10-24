#TODO: улучшить тесты
import json
import requests

from pydantic import ValidationError


from src.models.user import User
url = "http://127.0.0.1:8000/api/users/"
global_user = {
    "name": "alex",
    "salary": 300
}

def test_create_user():
    global global_user
    res = requests.post(url, json=global_user)
    _user = res.json()
    global_user["_id"] = _user['_id']
    print(global_user)
    # assert res.status_code == 200
    # assert _user == global_user

def test_get_user():
    res = requests.get(url + global_user["_id"])
    _user = res.json()
    print(_user == global_user)
    # assert _user == global_user

def test_get_users():
    res = requests.get(url)
    users =  res.json()
    # print(json.dumps(users, sort_keys=True, indent=4))
    if len(users) > 0:
        print(True)
        #assert True
    else:
        print(False)
        # assert False

def test_update_user():
    global global_user
    user = {
        "name": "bob",
        "salary": 800
    }
    res = requests.put(url + global_user["_id"], json=user)
    _user = res.json()
    user["_id"] = global_user["_id"]
    print(user["_id"] == _user["_id"])
    print(_user == user)
    global_user = user
    print('_user ', _user)
    print('user ', user)
    print('global_user ', global_user)
    # assert _user == user

def test_delete_user():
    print(global_user)
    res = requests.delete(url + global_user["_id"])
    _user = res.json()
    # del _user['_id']
    print(_user)
    #assert _user == global_user

test_create_user()
test_get_user()
test_get_users()
test_update_user()
test_delete_user()

