#!/usr/bin/env python3
# coding: utf-8

import json
import os

f = open('tmp1.json','w')

mon_dictionnaire = {"Voiture":"Yaris","Moteur":"4ch","Portes":5}
print(mon_dictionnaire)
print(type(mon_dictionnaire))

j = json.dump(mon_dictionnaire, f) #sauve le json dans le fichier texte 'f'
print(j)
print(type(j))
