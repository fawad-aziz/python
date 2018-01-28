import socket
import requests

print(socket.gethostname())
ip = socket.gethostbyname(socket.gethostname())

print(ip)

#url = 'http://usercountry.com/v1.0/json/' + ip
url = 'http://usercountry.com/v1.0/json/107.216.161.59'
print(url)

r = requests.get(url)
result = r.json()
if result['status'] == 'failure':
    print(result.error)
else:
    print(result['currency']['code'])
print(result)
