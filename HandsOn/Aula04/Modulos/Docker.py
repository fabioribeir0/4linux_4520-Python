#!/usr/bin/python
from Modulos.SSH import main_fn
from Modulos.Geral import read_db, write_db
import json


def create_cont(nome):
    cmd = 'docker run -tdi --name {0} debian /bin/bash'.format(nome)
    container = main_fn(cmd)
    return container


def rem_cont(nome):
    cmd = 'docker stop {0} && docker rm {0}'.format(nome)
    container = main_fn(cmd)
    return container

def ip_cont(nome):
    cmd = 'docker inspect {0}'.format(nome)
    ip = main_fn(cmd)
    ip = json.loads(ip)
    ip = ip[0].get('NetworkSettings').get('IPAddress')
    return ip
