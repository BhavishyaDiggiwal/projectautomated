#!/usr/bin/python36

print("content-type:text/html")
print("")
import subprocess as sp
x=sp.getoutput("sudo ansible-playbook /home/devops/ws/saas.yml")
print("x")

