import json
import requests
import jsonpath
user_data={
  "name": "somethingupdated",
  "job" : "somerandompositionupdate"
    }
#url="https://reqres.in/api/users/2"
#response=open("user_data.jason","r").read()
#json_response=response.json()
#response=requests.post('https://reqres.in/api/users',data=json.loads(user_data))
response=requests.put("https://reqres.in/api/users/2",data=user_data)
print(response)
print(response.json())
json_response=response.json()
assert json_response["name"]=="somethingupdated", "data is not same"
assert response.status_code==200, "data not get posted"
print(json_response["updatedAt"])

