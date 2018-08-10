#!/usr/bin/env python3
# coding: utf-8

import requests
import json

#Make API request
token = "?authtoken=9dX4CaNCJqkQNgsD2B3Z76ZxdmFaqKWl"
urlbase = "http://rundeck.virtual-expo.com/api/24"
url = urlbase + "/projects" + token
headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)

#Déclaration des dico
d_projet = dict()
d_job = dict()
d_element = dict()

#Loop on projects name.
for element in r.json():
    projet = element["name"]
    print("Projet -> " + projet)

    #Get job list
    urljoblist = urlbase + "/project/" + projet + "/jobs" + token
    #print(urljoblist)
    r2 = requests.get(urljoblist, headers=headers)
    l = r2.json() #r2.json() est une liste
    #print(json.dumps(r2.json()))

    #Boucle sur les job du projet
    for element in l: #element est un dictionnaire
        print(element["name"]) #j'ai bien le nom du job ici
        urljobexecutions = urlbase + "/job/" + element["id"] + "/executions" + token + "&max=1"
        #print("url job execution -> " + urljobexecutions)
        r3 = requests.get(urljobexecutions, headers=headers) #r3 est un dictionnaire
        d3 = r3.json() #d3 est un dictionnaire (clés : paging et executions)
        #print(d3)
        #print(urljobexecutions)
        if d3["executions"] != "":
            for valeurs in d3["executions"]: #ici valeurs est un dictionnaire
                print(valeurs["status"])
                if "successfulNodes" in valeurs: print(f'Node(s) en succès -> {valeurs["successfulNodes"]}')
                if "failedNodes" in valeurs: print(f'Node(s) en fail -> {valeurs["failedNodes"]}')
                if "date-started" in valeurs: print(valeurs["date-started"]["date"])
                if "date-ended" in valeurs: print(valeurs["date-ended"]["date"])
                if "user" in valeurs: print(valeurs["user"])
                final[element["name"]] = valeurs["date-started"]["date"]
                print(final)
                # if valeurs["successfulNodes"] : print(valeurs["successfulNodes"])
                # if valeurs["date-ended"]["date"] : print(valeurs["date-ended"]["date"])
                # if valeurs["status"] == "succeeded":
                #     print(valeurs["date-ended"]["date"])
                #     print(valeurs["successfulNodes"])
                # else:
                #     print(valeurs["failedNodes"])

        print("+++++++++++++++++")
    print("*************************************")

#mon container de dev
#docker run -p 4440:4440 -e EXTERNAL_SERVER_URL=http://localhost:4440 --name rundeck -t jordan/rundeck:latest
#curl -H "Accept:application/json" http://localhost:4440/api/2/projects?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu[{"url":"http://localhost:4440/api/24/project/mon-premier-projet","name":"mon-premier-projet","description":""}]

#curl -H "Accept:application/json" http://rundeck.virtual-expo.com/api/24/project/backup-dblx-mysql/jobs?authtoken=9dX4CaNCJqkQNgsD2B3Z76ZxdmFaqKWl |python -m json.tool
