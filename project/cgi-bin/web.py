#!/usr/bin/python36

import subprocess as sp
print("content-type: text/html\n")
print("<i> hello prabhat</i>")
print(sp.getoutput("/usr/bin/date"))

print(sp.getoutput("/usr/bin/whoami"))
#print(sp.getoutput("su - apache"))
print(sp.getoutput("sudo useradd prab"))
