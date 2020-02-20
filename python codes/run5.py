#!/usr/bin/python36
print("content-type:text/html")
print("location: http://192.168.43.230/cgi-bin/run.py")
print("")

import cgi
import subprocess as sp

data=cgi.FieldStorage()
c=data.getvalue("a")
d=data.getvalue("b")
os=sp.getoutput("sudo docker run -dit --name {} {}  ".format(c,d))
print(os)
