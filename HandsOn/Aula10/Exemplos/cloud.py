#!/usr/bin/python

from servidor import Servidor
from VNC import VNC


class Cloud(Servidor, VNC):
    pass

    def __init__(self):
        self.cpu = 1
        self.memoria = 512
        self.disco = 50


if __name__ == '__main__':
    c = Cloud()
    c.contratar_cpu()
    c.contratar_memoria()
    c.contratar_disco()
    print c.cpu
    print c.memoria
    print c.disco
    c.acesso()
