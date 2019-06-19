#importing python modules
import subprocess as sp

#variables
conname="disti"
ifnam="enp0s3"
typ="ethernet"
ip="192.168.43.88/24"
gw="192.168.43.1"
dns="192.168.43.1"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/staticvars.yml",mode='w')

#writing varibles in file
fp.write('conname: "{}"\n'.format(conname))
fp.write('ifnam: "{}"\n'.format(ifnam))
fp.write('type: "{}"\n'.format(typ))
fp.write('dns: "{}"\n'.format(dns))
fp.write('ip: "{}"\n'.format(ip))
fp.write('gw: "{}"\n'.format(gw))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook staticip.yml")

