#!/usr/bin/env python
#coding:utf-8

import json
import requests
fichero=open ("fichero.txt","w")

cantante = raw_input('Search artist:')
#url='http://api.deezer.com/search?'
#params={q:'%s'%cantante}
#identificador_artista=[]


respuesta=requests.get('http://api.deezer.com/search?q=%s'% cantante)
datos=respuesta.text.encode('utf-8')
dicc_api=json.loads(datos)
raiz=dicc_api["data"]
for i in raiz:
    titulo=i["title"]
    id_album=i["album"]["id"]  
    enlace=i["link"]
    print titulo
    print id_album
    print enlace  
    fichero.write(titulo)
    fichero.write(enlace)
