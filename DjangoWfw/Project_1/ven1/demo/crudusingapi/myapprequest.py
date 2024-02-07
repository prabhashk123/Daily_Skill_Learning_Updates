# this is a 3rd party  application  anyone like java,python,js
# it is not part of web application only testing api
import requests
import json

URL="http://127.0.0.1:8000/crudusingapi/api/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)
# get_data(4)
get_data()

# for create
def post_data():
    data={
        'name':'Prabhash kumar',
        'roll':20,
        'city':'Indore',
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)
# post_data()

def update_data():
    data={
        'id':1,
        'name':'Prahlad Kumar Bhagat',
        'city':'Rupoli',
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data)
    data=r.json()
    print(data)
# update_data()

# delete data
def delete_data():
    data={'id':4}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
# delete_data()
