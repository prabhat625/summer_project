#importing python modules
import subprocess as sp

#variables
username="chits"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/uservar.yml",mode='w')

#writing varibles in file
fp.write('username: "{}"\n'.format(username))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook user.yml")

