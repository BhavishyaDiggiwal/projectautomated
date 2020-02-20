#!/usr/bin/python36

print("content-type:text/html")
print("")
import subprocess as sp
a=sp.getoutput("sudo ansible-playbook http.yml")
print(a)
