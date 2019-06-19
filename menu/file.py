#importing python modules
import subprocess as sp

#variables
filepath="/root/Desktop/diti.txt"
own="root"
grp="root"
mod="0755"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/filevar.yml",mode='w')

#writing varibles in file
fp.write('filepath: "{}"\n'.format(filepath))
fp.write('own: "{}"\n'.format(own))
fp.write('grp: "{}"\n'.format(grp))
fp.write('mod: "{}"\n'.format(mod))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook file.yml")

