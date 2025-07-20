import requests
# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.json()

latu=19.075983
longu=72.877655
# response=requests.get(url="https://api.kanye.rest")
# print(response.json())
parameters={"lat":latu,
            "lng":longu  }
response=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())