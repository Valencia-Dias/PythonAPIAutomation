import requests
import json

headers1 = {
    'Accept':'text/plain'
}

baseURl = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'
def getRequest():
    response = requests.get(baseURl,headers=headers1)
    res = response.json()
    assert response.status_code == 200,'Status code is not matching'
    userId  = res[0]['id']
    return userId


def getRequestOfUser():
    id = getRequest()
    response = requests.get(baseURl+'/'+id)
    print(response.url)
    # print(response.json())


getRequestOfUser()