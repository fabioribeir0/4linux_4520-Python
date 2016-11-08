#!/usr/bin/python

def ls(*args):          #Se o paramentro nao for obrigatorio: ls(args='')`
    print args

ls('ls')
ls('ls','-','l')
ls('ls','-','l','a')
ls(1,2,3,4)

def api(**kwargs):      #Dicionarios. kwargs = keyword arguments
    print kwargs
    print kwargs.get('username')
    print kwargs.get('email')

api(username='fabio.ribeiro',email='fabio_ribeiro@icloud.com')
