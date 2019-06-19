#importing python modules
import subprocess as sp

#variables
host="disti.localdomain"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/hostvar.yml",mode='w')

#writing varibles in file
fp.write('host: "{}"\n'.format(host))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook hostname.yml")

