#!/usr/bin/python
from Modulos.SSH import SSH
from Modulos.Geral import read_db, write_db
import json


class Docker(SSH):


    def create(self, nome):
        cmd = 'docker run -tdi --name {0} debian /bin/bash'.format(nome)
        container = self.send_cmd(cmd)
        return container


    def rem(self, nome):
        cmd = 'docker stop {0} && docker rm {0}'.format(nome)
        container = self.send_cmd(cmd)
        return container


    def ip(self, nome):
        cmd = 'docker inspect {0}'.format(nome)
        ip = self.send_cmd(cmd)
        ip = json.loads(ip)
        ip = ip[0].get('NetworkSettings').get('IPAddress')
        return ip
