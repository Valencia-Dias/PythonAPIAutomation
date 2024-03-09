import requests
import json

headers1 = {
    'Accept':'text/plain',
    'Content-Type':'application/json'
}
requestbody =    {
  "id": 15,
  "title": "val",
  "dueDate": "2024-03-09T00:56:16.973Z",
  "completed": True
}
baseURl = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

# Before update
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/1')
print('Before update ',response.json())

#After update
def putRequest():
    response = requests.post(baseURl,headers=headers1,json=requestbody)
    res =response.json()
    print(res)
    assert response.status_code == 200,'Status code is not matching'
    # id = res['id']
    # assert id == 100,'Id is not matching'


putRequest()