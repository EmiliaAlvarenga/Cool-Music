#!/usr/bin/env python
#coding:utf-8

import json
import requests
from bottle import route, get, post, run, template, debug, error
import bottle 


#por si escribo mal una direccion
@error(404)
def error404(error):
    return 'Nada que mostrar aqui'

#Pedimos el nombre del artista para usarlo como parametro el la peticion	
@get('/search')
def search():
    return '''
        <form action="/search" method="post">
            Artista: <input name="artista" type="text" />
            <input value="Search" type="submit" />
        </form>
    '''

#¿como capturar el nombre del artista para pasarla al template?
@post('/search')
def nombre():
    global artista
    title=[]
    artista = request.forms.get('artista')
    respuesta=requests.get('http://api.deezer.com/search?q=%s'% artista)
    datos=respuesta.text.encode('utf-8')
    dicc_api=json.loads(datos)
    raiz=dicc_api["data"]
    for i in raiz:
	tlista=i["title"]
	title.append(tlista)
	return template('index', artista=artista, title=title)

 
run(host='localhost', port=8080, debug=True, reloader=True)

