import requests
import json
import jsonpath

response=requests.delete("https://reqres.in/api/users/2")
print(response.status_code)

assert response.status_code == 204, "user is not deleted"
