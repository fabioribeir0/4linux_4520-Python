#!/usr/bin/python


class Servidor:
    cpu = 0
    memoria = 0
    disco = 0


    def contratar_cpu(self):
        self.cpu += 1


    def contratar_memoria(self):
        self.memoria += 1024


    def contratar_disco(self):
        self.disco += 10
