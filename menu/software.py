#importing python modules
import subprocess as sp

#variables
packname="httpd"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/softvars.yml",mode='w')

#writing varibles in file
fp.write('packname: "{}"\n'.format(packname))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook software.yml")

