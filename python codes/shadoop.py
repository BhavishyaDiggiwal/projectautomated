#!/usr/bin/python36

print("content-type:  text/html")
print()

import subprocess as sp
import cgi

data=cgi.FieldStorage()
print("""
<form action="http://192.168.43.42/cgi-bin/shadoop.py">
<input type='text' placeholder='Enter slave IP' name='slave'/>
<input type='text' placeholder='Enter slave name' name='sname'/>
<input type='submit' value='submit'/>
</form>
""")
print("hey")

slave=data.getvalue('slave')
sname=data.getvalue('sname')
print(slave)

# Now copy and save a copy of the ansible hosts file somewhere. This code will be editing it and we will need a backup file later
#replace "myhosts" in the next line with wherever the ansible host file is and add "[slaves]" in the last line follwed by NOTHING

print(sname)
var = sp.getoutput("sudo echo '{}' >> /var/www/cgi-bin/myhosts".format(slave))
sp.getoutput("sudo echo '{}  {}' >> /var/www/cgi-bin/Hadoop/hosts".format(slave,sname))
print("<a href=http://192.168.43.42/cgi-bin/hadoop.py> Go Back </a>")
