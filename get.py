import json
import requests
import jsonpath
response=requests.get("https://reqres.in/api/users?page=2")
print(response)
print(type(response))
print(response.content)
#print(response.text)
#print(response.url)
jsonresponse=response.json()
print(jsonresponse)
print(jsonresponse['total_pages'])
assert jsonresponse['total_pages']==2,"total pages are not correct"
print(jsonresponse['data'][3]['avatar'])
assert jsonresponse['data'][3]['avatar'].endswith("image.jpg"), "image type is not there"




