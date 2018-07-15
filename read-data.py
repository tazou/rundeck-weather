#!/usr/bin/env python3

import requests
import json

url = "http://localhost:4440/api/24/projects?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu"
headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)

print(type(r)) #<class 'requests.models.Response'>
print(r.json)

# Boucle sur le nom de chaque projets.
for element in r.json():
    print(element["name"])

#GET  project's jobs
urljob = "http://localhost:4440/api/24/project/mon-premier-projet/jobs?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu"
headers = {'Accept': 'application/json'}
r1 = requests.get(urljob, headers=headers)
print(r1.json())

#GET job's info
jobid = "af266d96-8ba1-4286-b356-7e037fc5315c"
urljob1 = "http://localhost:4440/api/24/job/" + jobid + "?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu"
print(urljob1)
headers = {'Accept': 'application/json'}
r2 = requests.get(urljob1, headers=headers)
print(r2.json())


#status de l'exécution d'un projet :
#http://localhost:4440/api/24/project/mon-premier-projet/executions?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu


# print(type(r.json())) #r.json() renvoi une liste  <class 'list'> contenant un dico qui contient le json
# print(r.json())
# print(r.json()[0])
# print(type(r.json()[0])) # ici c'est un dict
# mon_dictionnaire = r.json()[0]
# print(mon_dictionnaire)
#
# print(r.json()[0]["name"]) #ici nom du projet
#
# for element in r.json()[0].keys():
#     print(r.json()[element]["name"])

#j = json.load(r.json()[0])
#print(j['name'])

#j = json.load(r.json())
#print(j['name'])

# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
# print(j)
# print(j['two'])

#http://docs.python-guide.org/en/latest/scenarios/json/

#url = 'https://api.github.com/some/endpoint'
#>>> headers = {'user-agent': 'my-app/0.0.1'}
#>>> r = requests.get(url, headers=headers)

#http://docs.python-requests.org/en/master/user/quickstart/

#mon container de dev
#docker run -p 4440:4440 -e EXTERNAL_SERVER_URL=http://localhost:4440 --name rundeck -t jordan/rundeck:latest

#curl -H "Accept:application/json" http://localhost:4440/api/2/projects?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu[{"url":"http://localhost:4440/api/24/project/mon-premier-projet","name":"mon-premier-projet","description":""}]
