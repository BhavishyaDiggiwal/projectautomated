#!/usr/bin/python36

print("content-type:text/html")
print("")
import cgi
import subprocess as sp

mydata=cgi.FieldStorage()
b=mydata.getvalue('q')
a=sp.getoutput("sudo useradd " + b)
print(a)
