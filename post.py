import json
import requests
import jsonpath
user_data={
  "name": "something",
  "job" : "somerandomposition"
   }
#url='https://reqres.in/api/users'
#response=open("user_data.jason","r").read()
#json_response=response.json()
#response=requests.post('https://reqres.in/api/users',data=json.loads(user_data))

response=requests.post('https://reqres.in/api/users',data=user_data)
print(response)
print(response.json())
json_response=response.json()
assert json_response["name"]=="something", "data is not same"
assert response.status_code==201, "data not get posted"

print(json_response["id"])