<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Cool-Music</title>
        <link rel="stylesheet" type="text/css" href="css/hojaestilo.css">
    </head>
    <body>
	<h3>Album infoimation</>
	%cont=1
	%for i in data["data"]:
	    <div id="colorres">
		<ol>Artista {{ i['artist']['name'] }} </ol>
		<ul>Album: {{ i['title'] }}</ul>
		<img src="{{ i['cover'] }}"/>
		<p><a href="{{ i['link'] }}"> Escuchar este album </a></p>
	    </div>
	%cont=cont+1	
	%end	
	<a href="/home">Inicio</a>	
    </body>
</html>
