#!/usr/bin/python36

print("content-type:text/html")
print("")

import cgi
import subprocess as sp

#data=cgi.FieldStorage()
#name=data.getvalue('q')
a=sp.getoutput("sudo docker images")
print("<select>")
for i in a.split("\n")[1:]:
	j=i.split()
	print("<option>"+j[0]+":"+j[1]+"</option>")
print("</select>")
