#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp

#Take a Backup of your ansible host file - lets call it defaultHost
#This is done because once this program has been run, we will have to reset the hosts file to avoid problems in the future
#Let the hosts file be hosts


#Uncomment the following and add the locations
#sp.getoutput("cp /location/defaultHost /location/hosts")

#The following is done to reset the main hostfile (the one which contains IPs and their names)
sp.getoutput("cat hostnames > ./Hadoop/hosts")

