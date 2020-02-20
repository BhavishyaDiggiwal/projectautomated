import os
import subprocess as sp
while True:
  print("############ MENU #############")
  print("1. Launch ec2 instance")
  print("2. Launch s3 instance")
  print("3. Send Email")
  print("4. Set up LVM")
  print("5. Launch Docker")
  print("6. Set up Web Server")
  print("7. Set up Hadoop")
  print("8. Exit")

  ch = input("Enter your choice : ", end=' ')
  

  if(ch==1):
	os.system("ansible-playbook ec2.yml")
	os.system("tput setaf 2")
	print("Instance Launched Successfully")
	os.system("tput setaf 0")
  if(ch==2):
	os.system("ansible-playbook s3.yml")
        os.system("tput setaf 2")
        print("Instance Launched Successfully")
        os.system("tput setaf 0")
  if(ch==3):
	os.system("ansible-playbook mail.yml")
        os.system("tput setaf 2")
        print("Mail Sent Successfully")
        os.system("tput setaf 0")
  if(ch==4):
  if(ch==5):
	os.system("ansible-playbook docker.yml")
        os.system("tput setaf 2")
        print("Docker Launched Successfully")
        os.system("tput setaf 0")
  if(ch==6):
  if(ch==7):
	os.system("ansible-playbook ./Hadoop/master.yml")
        os.system("ansible-playbook ./Hadoop/slave.yml")
        os.system("tput setaf 2")
        print("Hadoop Setup Successful")
        os.system("tput setaf 0")
  if(ch==8):
	exit
