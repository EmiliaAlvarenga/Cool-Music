<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Cool-Music</title>
    </head>
    <body>
        <h3>Resultados de la búsqueda</h3>
        %for i in data['data']:
         <p>Artista {{i['artist']['name']}} </p>
         <p>Album: {{i['title']}}</p>
         <img src="{{i['cover']}}"/>
         <p><a href="{{i['link']}}"> Escuchar este album </a></p>
        %end
        <a href="/artist">Realice otra búsqueda</a>
    </body>
</html>
