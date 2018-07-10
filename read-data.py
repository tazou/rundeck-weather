#!/usr/bin/env python3

import requests
import json

url = "http://localhost:4440/api/1/projects?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu"
headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)

#print(r.status_code)
#print(r.headers)
#print(r.content)
#print(r.json())
#print("-----")
#a=r.json()
#print(json.dumps(a))
data = json.loads(r.content.decode())
print(type(data))
print(data[0]['name'])

for a, b in enumerate(data):
  for key, val in b.items():
    print(val)

#http://docs.python-guide.org/en/latest/scenarios/json/

#url = 'https://api.github.com/some/endpoint'
#>>> headers = {'user-agent': 'my-app/0.0.1'}
#>>> r = requests.get(url, headers=headers)

#http://docs.python-requests.org/en/master/user/quickstart/

#mon container de dev
#docker run -p 4440:4440 -e EXTERNAL_SERVER_URL=http://localhost:4440 --name rundeck -t jordan/rundeck:latest

#curl -H "Accept:application/json" http://localhost:4440/api/2/projects?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu[{"url":"http://localhost:4440/api/24/project/mon-premier-projet","name":"mon-premier-projet","description":""}]
