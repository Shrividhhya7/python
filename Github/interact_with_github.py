import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

output=response.json()

for detail in range(len(output)):
    print(output [detail]["user"] ["login"])