import subprocess as sp
sp.getoutput("sudo yum install tiger-vnc server -y")
sp.getoutput("sudo useradd adi6")
sp.getoutput("sudo cp vncserver@:5.service /etc/systemd/system/")
sp.getoutput("sudo systemctl daemon-reload")
sp.getoutput("sudo ssh adi6@192.168.43.230 vncserver | echo redhat")
sp.getoutput("sudo systemctl restart vncserver@:5")
