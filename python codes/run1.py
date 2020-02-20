#!/usr/bin/python36
print("content-type:text/html")
print("location: http://192.168.43.230/cgi-bin/run.py")
print("")

import cgi
import subprocess as sp
data=cgi.FieldStorage()
a=data.getvalue("s")
os=sp.getoutput("sudo docker start {}".format(a))
print(os)
