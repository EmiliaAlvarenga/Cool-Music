<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Cool-Music</title>
	<link rel="stylesheet" type="text/css" href="static/hojaestilo.css">
    </head>
    <body>
    <div id="contenedor"> 
        <h2>Resultados de la búsqueda</h2>
        %for i in data['data']:
            <div class="capsula">
	    <table border="0" id="colorres" >
	        <tr>
	            <td>
		        <p><img src="{{ i['cover'] }}" /></p>
	                <td>
	                    <p>{{ i['artist']['name'] }} </p>
		            <p>{{ i['title'] }}</p>
			    <a href="{{ i['link'] }}"> Escuchar este album </a>
		        </td>
		    </td>
		    <br>
	        </tr>
	        <br>
	    </table>		
            </div>
        %end
	<div class="redirect">
	    <a href="/artist">Realice otra búsqueda</a> 
	</div>
    </div>
    </body>
</html>
