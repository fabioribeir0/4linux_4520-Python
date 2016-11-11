#!/usr/bin/python
from Modulos.SSH import SSH


class Docker(SSH):

    def criar(self, nome, imagem):
        cmd = 'docker run -tdi --name {0} {1} /bin/bash'.format(nome, imagem)
        self.executar_comando(cmd)
