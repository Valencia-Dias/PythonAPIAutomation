import requests
from faker import Faker

#Create data using faker library
fake = Faker()
name = fake.name()
email = fake.email()


headers1 = {
    'Content-Type':'application/json',
    'Authorization':'Bearer f46f26a9ad455a56d18b494d4cfbab065a0a999f9ff016da1d8b9a61b482210a'
}
requestbody ={
  
    "name": name,
    "email": email,
    "gender": "male",
    "status": "inactive"
}
print(requestbody)

baseURl = 'https://gorest.co.in/public/v2/users'
response = requests.post(baseURl,headers=headers1,json=requestbody)
print(response.status_code)
assert response.status_code == 201,"Resource not created"


getResponse = requests.get(baseURl+'/'+str(response.json()['id']),headers=headers1)
print(getResponse.url)
print(getResponse.json())