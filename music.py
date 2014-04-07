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
#for i in raiz:
ident=raiz[1]["album"]["title"] ##Esto funciona, pero como poner el titulo de album de cada uno de los objeto de la lista data?? 
#identificador_artista.append(ident)
#link=dicc_api["link"]
print ident 
fichero.write(ident)
#print link
