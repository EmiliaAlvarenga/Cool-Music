#!/usr/bin/env python
#coding:utf-8

import json
import requests
from bottle import route, get, post, run, template, debug, error, request
import bottle 


#por si escribo mal una direccion
@error(404)
def error404(error):
    return 'Nada que mostrar aqui'

@route('/home')
def search():
    return template('index')

    
#Pedimos desde template el nombre del artista para usarlo como parametro el la peticion	
@route('/artist')
def search_name():
	return template('artist')   
    
#¿como pasar los datos al template?
		
@post('/info')
def nombre():
	global artist
	artista = request.forms.get("artista")
	respuesta = requests.get('http://api.deezer.com/search?q=%s'% artista)
	datos=respuesta.text.encode('utf-8')
	dicc_api=json.loads(datos)
	raiz=dicc_api["data"]
	title=[]
	for i in raiz:
		tlista=i["title"]
		title.append(tlista)
		return template('results', title=title)

debug(True)
run(host='localhost', port=8080, reloader=True)

 
run(host='localhost', port=8080, debug=True, reloader=True)

