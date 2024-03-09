import requests
import json

headers1 = {
    'Accept':'text/plain',
    'Content-Type':'application/json'
}
requestbody =    {
  "id": 100,
  "title": "string",
  "dueDate": "2024-03-09T00:22:33.275Z",
  "completed": True
}

baseURl = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

def postRequest():
    response = requests.post(baseURl,headers=headers1,json=requestbody)
    res =response.json()
    assert response.status_code == 200,'Status code is not matching'
    id = res['id']
    assert id == 100,'Id is not matching'












postRequest()