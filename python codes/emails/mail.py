#!/usr/bin/python36

print("content-type: html/text")
print("")

import cgi 
import subprocess as sp 

a= sp.getoutput("ansible-playbook /var/www/cgi-bin/emails/mail.yml")
print(a)
