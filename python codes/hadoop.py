#!/usr/bin/python36

print("content-type:  text/html")
print()

#link for master node details
print("<a href=http://192.168.43.42/cgi-bin/mhadoop.py> Enter Master Node details here </a> <br>")

#linkk for slave node details
print("<a href=http://192.168.43.42/cgi-bin/shadoop.py> Enter Slave nodes details here </a> <br>")

#Now all the hosts files are set as needed
#Use this link to reset 
print("<a href=http://192.168.43.42/cgi-bin/hreset.py> Click to reset </a> <br>")

#Link to run the playbooks
print("""If you have successfully entered the node details
<a href=http://192.168.43.42/cgi-bin/hadooprun.py> Set up Hadoop </a>
""")
