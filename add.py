#coding:utf-8
import io,sys

def inp(txt):
    vp=sys.version_info
    if vp[0]==2: return raw_input(txt)
    else: return input(txt)

c="#"
cc="|"
ccc=","

def add():
    nom=inp("nom : ")
    lien=inp("lien zip : ")
    description=inp("description : ")
    requirements=inp("requirements (',' to separate) : ")
    lien_version=inp("lien version : ")
    txt=cc+nom+c+lien+c+description+c+requirements+c+lien_version
    f=open("data.nath","a")
    f.write(txt)
    f.close()

add()

