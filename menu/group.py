#importing python modules
import subprocess as sp

#variables
grpname="dd"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/groupvar.yml",mode='w')

#writing varibles in file
fp.write('grpname: "{}"\n'.format(grpname))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook group.yml")

