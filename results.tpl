<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Cool-Music</title>
    </head>
    <body>
        <h1>{{ artist }}</h1>
        %for i in title:
            <ul>
	        <li>{{ title }}</li>
            </ul>
            <a href="/home">Homepage</a> 	
    </body>
</html>
