#!/usr/bin/env python3
# coding: utf-8
# Fait en python 3.6

path = 'test.html'
file = open(path,'w')

title = '<h1>Rundeck</h1>'
body = "<p>Bonjour tout le monde"
msg = title + body

file.write(msg)
file.close()
