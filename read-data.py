#!/usr/bin/env python3
# coding: utf-8
# Fait en python 3.6

import requests
import json

#Requête de l'API Rundeck pour les projets
token = "?authtoken=UGpUyHm9MqS7swx7xewWMpoo6Zia9PaJ" #Il faudra externaliser le token et en générer un nouveau après le dev puis révoquer celui ci.
urlbase = "http://rundeck.virtual-expo.com/api/24"
url = urlbase + "/projects" + token
headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)
#print(url)

#Déclaration des dico
d_projet = dict()
d_job = dict()
d_element = dict()
final = dict()
f = dict()
t2 = dict()
listejobs = list()
i = 0

#Loop on projects name.
for element in r.json():
    projet = element["name"]
    #print("Projet -> " + projet)

    #Récupérer la liste des jobs
    urljoblist = urlbase + "/project/" + projet + "/jobs" + token
    #print(urljoblist)
    r2 = requests.get(urljoblist, headers=headers)
    l = r2.json() #r2.json() est une liste
    #print(json.dumps(r2.json()))

    #Boucle sur les job du projet
    for element in l: #element est un dictionnaire
        job_name = element["name"]
        #print("nom du job -> " + job_name) #j'ai bien le nom du job ici
        urljobexecutions = urlbase + "/job/" + element["id"] + "/executions" + token + "&max=1"
        #print("url job execution -> " + urljobexecutions)
        r3 = requests.get(urljobexecutions, headers=headers) #r3 est un dictionnaire
        d3 = r3.json() #d3 est un dictionnaire (clés : paging et executions)
        #print(d3)
        #print(urljobexecutions)
        if d3["executions"] != "":
            for valeurs in d3["executions"]: #ici "valeurs" est un dictionnaire
                #print(valeurs["status"])
                #if "successfulNodes" in valeurs: print(f'Node(s) en succès -> {valeurs["successfulNodes"]}')
                if "successfulNodes" in valeurs:
                    #print("Node(s) en succès -> {} ".format(valeurs["successfulNodes"]))
                    nodeSucces = valeurs["successfulNodes"]
                else:
                    nodeSucces = "Aucun"
                if "failedNodes" in valeurs:
                    #print("Node(s) en fail ->  {} ".format(valeurs["failedNodes"]))
                    nodeFail = valeurs["failedNodes"]
                else:
                    nodeFail = "Aucun"
                #if "date-started" in valeurs: print(valeurs["date-started"]["date"])
                #if "date-ended" in valeurs: print(valeurs["date-ended"]["date"])
                #if "user" in valeurs: print(valeurs["user"])
                d_job[job_name] = {"status":valeurs["status"],
                                            "nodeS":nodeSucces,
                                            "nodeF":nodeFail,
                                            "datedebut":valeurs["date-started"]["date"],
                                            "datefin":valeurs["date-ended"]["date"]}
                #listejobs.append(d_job)
                #print("la liste -> {}".format(listejobs))


        #print("++++++for jobs+++++++++++")

    #Fin du for job
    i += 1
    #print("le dico d_job -> ")
    # for k,v in d_job.items():
    #     print("Voici la clé -> {}".format(k))
    #     print("Voici la valeur -> {}\n".format(v))

    final[projet] = d_job
    #final[projet] = d_job
    #print("\nle dico FINAL du projet -> {}".format(projet))
    #print(final)
    #del listejobs[:]

    #print("\n***********for projects**************************")
    #print(json.dumps(final))
    d_job = {}

    if i == 2:
        #print("le dico final dans le if")
        #print(final)
        break

#Construction du html
#print("---------html-----------")
# for p,j in final.items():
#     print("<h1>{}</h1>".format(p))
#     for k,job in j.items():
#         print("<b>{}</b>".format(k))
#         print("<ul>")
#         for t in job.items():
#             print("<li>{}</li>".format(t))
#         print("</ul>")

debut_html = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <title>Rundeck Weather</title>
  </head>
  <body>
    <h1>Rundeck Weather</h1>
    <h5>Page générée le 28/08/2018 à 13:37</h5>
    <script src="js/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="js/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

"""

#Boucle sur le nombre de projets
for ligne_html in final.items():
    debut_html += """
    <div class="container">
      <div class="row">
    """
    for p,j in final.items():
        debut_html += """
        <!--debut loop projet-->
        <div class="col-sm">
        <table class="table">
        <thead class="thead-dark">
        <tr>
        <th>{}</th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        </tr>
        </thead>
        <tbody>
        """.format(p)
        for k,job in j.items():
            debut_html += """
              <tr>
            <th scope="row">{}</th>""".format(k)
            for t in job.items():
                debut_html += """
                <td class="bg-success">{}</td>
                """.format(t)
            debut_html += "</tr>"


path = 'test.html'
file = open(path,'w')

title = '<h1>Rundeck</h1>'
body = "<p>Bonjour tout le monde"
msg = title + body

file.write(debut_html)
file.close()

#mon container de dev
#docker run -p 4440:4440 -e EXTERNAL_SERVER_URL=http://localhost:4440 --name rundeck -t jordan/rundeck:latest
#curl -H "Accept:application/json" http://localhost:4440/api/2/projects?authtoken=4OxNnNOigtd8j729lki1Jj9FRoMLeQRu[{"url":"http://localhost:4440/api/24/project/mon-premier-projet","name":"mon-premier-projet","description":""}]

#curl -H "Accept:application/json" http://rundeck.virtual-expo.com/api/24/project/backup-dblx-mysql/jobs?authtoken=9dX4CaNCJqkQNgsD2B3Z76ZxdmFaqKWl |python -m json.tool
