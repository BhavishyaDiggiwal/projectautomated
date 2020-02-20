#!/usr/bin/python36

print("content-type:text/html")
print("")

import cgi
import subprocess as sp

#data=cgi.FieldStorage()
#name=data.getvalue('q')
a=sp.getoutput("sudo docker images")
print("<form action='http://192.168.43.230/cgi-bin/docker.py'>")
print("enter your docker name:<input name='n'/><br/>")
print("select your docker image")
print("<select name='img'>")
for i in a.split("\n")[1:]:
	j=i.split()
	print("<option>"+j[0]+":"+j[1]+"</option>")
print("</select>")
print("<br/><input type='submit'>")
print("</form>")
