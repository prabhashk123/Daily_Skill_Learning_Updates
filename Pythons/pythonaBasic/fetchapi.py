# import requests

# url = "https://api.example.com/data?param1=value1"
# response = requests.get(url)
# # Check for successful response
# if response.status_code == 200:
#   # Parse JSON data
#   data = response.json()
#   # Access and process specific data
#   print(data["key1"])
#   print(data["key2"])
# else:
#   print(f"Error: {response.status_code}")

# json api
# {
#     "userId": 1,
#     "title": "Buy milk",
#     "completed": false
# }
import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()
response.status_code
# If you don’t use the json keyword argument to supply the JSON data, then
# you need to set Content-Type accordingly and serialize the JSON manually. 
# Here’s an equivalent version to the previous code:
import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(url=api_url, data=json.dumps(todo), headers=headers)
response.json()
response.status_code

# Get Http request
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()