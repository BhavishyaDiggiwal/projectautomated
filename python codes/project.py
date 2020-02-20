#!/usr/bin/python36
print("content-type:text/html")
print("")
import cgi
import subprocess as sp

data=cgi.FieldStorage()
c=data.getvalue("a")
d=data.getvalue("b")

if c=="aditya" and d=="aditya1":
	print("<a href=http://192.168.43.230/menu.html><h1>CLICK HERE</h1></a>")

else:
	print("<a href='http://192.168.43.230/project.html'><center><h1>TRY AGAIN</h1></center></a>")
