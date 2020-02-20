#!/usr/bin/python36
print("content-type:text/html")
print("")

import cgi
import subprocess as sp

form=cgi.FieldStorage()
docker_name = form.getvalue("n")
docker_imag=form.getvalue("img")
a=sp.getoutput("sudo docker run -dit --name {} {}".format(docker_name,docker_imag))
print(a)
