<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Cool-Music</title>
    </head>
    <body>
	<h3>Album info</>
	%cont=1
	%for i in datos["data"]:
	    <ul>
	        <li>Artist {{ i['artist']['name'] }} </li>
		<li>Album {{ i['title'] }}</li>
		<img src="{{ i['cover'] }}"/>
		<p><a href="{{ i['link'] }}"> Listen this album </a></p>
	    </ul>
	%cont=cont+1	
	%end	
	<a href="/home">Homepage</a> 	
    </body>
</html>
