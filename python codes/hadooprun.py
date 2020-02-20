#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp

print("Setting up Hadoop Cluster")
sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop/master.yml")

sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/Hadoop/slave.yml")

sp.getoutput("cp ../myhosts_default ../myhosts")
