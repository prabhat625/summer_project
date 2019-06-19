#importing python modules
import subprocess as sp

#variables
name= "httpd"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/servicevar.yml",mode='w')

#writing varibles in file
fp.write('name: "{}"\n'.format(name))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook service.yml")

