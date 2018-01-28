import requests
import json

url = "https://qa4-rc.aprimo.com/api/oauth/create-native-token"

headers = {
    'client-id': "L4AIEHMR-FJSP",
    'authorization': "Basic bG9hZHVzZXI0OTpjZjRhYTExMjM2OTY0YThhYWFkYzE2NWEzYTc1OGQxNQ==",
    'cache-control': "no-cache",
    'postman-token': "b48d3e46-8538-d486-abed-fd1a73392c43"
    }

try:
    response = requests.request("POST", url, headers=headers)
    token = response.json()
    print(token['accessToken'])
except:
    print('error')
