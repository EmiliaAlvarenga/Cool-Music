#!/usr/bin/env python
#coding:utf-8

import json
import requests
from bottle import route, get, post, run, template, debug, error, request, static_file, default_app, TEMPLATE_PATH
import bottle
import os

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@error(404)
def error404(error):
    return 'Nada que mostrar aqui'

@route('/')
def search():
    return template('index')

@get('/artist')
def search_name():
    return template('artist')

		
@post('/info')
def nombre():
	global artist
	artist = request.forms.get("artista")
	r = requests.get('http://api.deezer.com/search/album', params={'q':'%s'% artist})
	dicc_api=json.loads(r.text)
	return template('results', data=dicc_api)


# This must be added in order to do correct path lookups for the views

#ON_OPENSHIFT = False
#if os.environ.has_key('OPENSHIFT_REPO_DIR'):
#    ON_OPENSHIFT = True

#if ON_OPENSHIFT:
#    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
#                                      'app-root/repo/wsgi/views/'))

#    application=default_app()
#else:

debug='TRUE'
run(host='localhost', port=8080)




