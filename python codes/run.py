#!/usr/bin/python36
print("content-type:text/html")
print("")

print("""<html>
<head>
<style>
body {background-image: url("http://192.168.43.230/docker.png")}
</style></head>
<body>""")
import subprocess as sp
os=sp.getoutput("sudo docker ps -a")
y=os.split("\n")
b=y[0].split()
c=b[2]
d=b[-3]
e=b[-1]
print("""
<table border='6' width=100%>
<tr><h3>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>START</td>
<td>STOP</td>
<td>TERMINATE</td></h3>
</tr>""".format(e,c,d))
for i in y[1:]:
	a=i.split()
	f=a[1]
	g=a[6]
	h=a[-1]
	print("""
	<tr>
	<td style>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.43.230/cgi-bin/run1.py?s={}'>START</a></td>
	<td><a href='http://192.168.43.230/cgi-bin/run3.py?s={}'>STOP</a></td>
	<td><a href='http://192.168.43.230/cgi-bin/run4.py?s={}'>Terminate</a></td>
	</tr>""".format(h,f,g,h,h,h))
print("</table><br/>")
print("<font color='red'><h><b>lIST OF DOCKER IMAGES PRESENT IN THE SYSTEM</b></h>")
z=sp.getoutput("sudo docker images")
dimage=z.split("\n")
o=dimage[0].split()
p=o[0]
q=o[1]
print("""<table border='6' width=50%>
<tr>
<td><b><h>{}</h><b></td>
<td><b><h>{}</h><b></td>
</tr>""".format(p,q))
for i in dimage[1:]:
	t=i.split()
	r=t[0]
	s=t[1]
	print("""<tr>
	<td>{}</td>
	<td>{}</td>
	</tr>""".format(r,s))
print("</table>")

print("<br/>")
print("<font color='red'><b>Here you can launch your own docker</b></font><br/>")
print("""<form action='http://192.168.43.230/cgi-bin/run5.py'><table border='6' width=100%>
<tr>
<td>name of os</td>
<td>image of os</td>
</tr>
<tr>
<td><input name='a'/></td>
<td><input name='b'/></td>
</tr>
</table><br/>
<input type='submit'/>
</form>""")
print("</body></html>")
