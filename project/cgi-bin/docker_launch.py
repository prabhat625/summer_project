#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")


form=cgi.FieldStorage()

name = form.getvalue("name")
img=   form.getvalue("img")

string ="sudo docker run -dit --name "+str(name)+" "+str(img)

x=sp.getoutput(string)

print("location: http://172.16.14.142/cgi-bin/docker.py\n")
