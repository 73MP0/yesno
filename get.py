import requests

URLs = "http://18.144.3.69"

r = requests.get(url = URLs)
data = r.json()

print(data)