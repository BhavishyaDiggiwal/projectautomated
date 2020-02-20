#!/usr/bin/python36

print("content-type:text/html")
print("")

import cgi
import subprocess as sp

data=cgi.FieldStorage()
name=data.getvalue("a")
if "date" in name:
	x=sp.getoutput("date")
	print(x)
elif "calender" in name:
	x=sp.getoutput("cal")
	print(x)
	
