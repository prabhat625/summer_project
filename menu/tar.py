#importing python modules
import subprocess as sp

#variables
filesrc="/root"
filedest="/root/Desktop/disti.tar.gz"
form="gz"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/tarvar.yml",mode='w')

#writing varibles in file
fp.write('filesrc: "{}"\n'.format(filesrc))
fp.write('filedest: "{}"\n'.format(filedest))
fp.write('form: "{}"\n'.format(form))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook archive.yml")
