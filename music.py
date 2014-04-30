#!/usr/bin/env python
#coding:utf-8

import json
import requests
from bottle import route, get, post, run, template, debug, error, request, static_file
import bottle 


#por si escribo mal una direccion
@error(404)
def error404(error):
    return 'Nada que mostrar aqui'
    
    
#Ruta de la hoja de estilo
@route('/css/:filename#.*#')
def server_static(filename):
    return static_file(filename, root='./css/')	

    
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
    artist = request.forms.get("artista")
    r = requests.get('http://api.deezer.com/search/album?q=%s'% artist)
    encode_utf8=r.text.encode('utf-8')
    dicc_api=json.loads(encode_utf8)
    data=dicc_api
    return template('results',artist=artist, data=data)

debug(True)
run(host='localhost', port=8080, reloader=True)

