# consume api using creating api url se means data read from url and call api from urls
api_url='http://127.0.0.1:8000/restapi/getcus/1'
import requests
import json

"""For serailzer data call api"""
# data=requests.get(api_url)
# data_json=data.json()
# print(data_json)

'''Deserialization me data list and dict so loop lagayenge call api'''
data=requests.get(api_url)
data_json=data.text
data_native=json.loads(data_json)
for e in data_native:
    print(e)
