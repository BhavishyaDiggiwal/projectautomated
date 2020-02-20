#!/usr/bin/python36

print("content-type:  text/html")
print()

import subprocess as sp

print("""
<form action=http://192.168.43.42/cgi-bin/mhadoop.py>
<input type='text' placeholder='Enter master IP' name='master'/>
<input type='submit' value='submit'/>
</form>
""")

import cgi

data=cgi.FieldStorage()
master=data.getvalue('master')

var = sp.getoutput("sudo echo 'ip: {}' > /var/www/cgi-bin/Hadoop/masterIP.yml".format(master))

sp.getoutput("sudo echo '{}  master.com' >> /var/www/cgi-bin/Hadoop/hosts".format(master))
print("""
<a href=http://192.168.43.42/cgi-bin/hadoop.py /> Go back </a>""")
