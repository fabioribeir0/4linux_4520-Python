#!/usr/bin/python

from servidor import Servidor
from IPMI import IPMI

class Fisico(Servidor, IPMI):


    def __init__(self):
        self.cpu = 4
        self.memoria = 2048
        self.memoria_ocupada = 1
        self.memoria_total = 4        
        self.disco = 1024
        self.disco_ocupado = 1
        self.disco_total = 4


    def contratar_cpu(self):
        print 'Faca um upgrade de maquina.'


    def contratar_memoria(self):
        if self.memoria_ocupada < self.memoria_total:
            self.memoria_ocupada += 1
            self.memoria += 2048
        else:
            print 'Voce nao tem mais slots de memoria disponiveis.'


    def contratar_disco(self):
        if self.disco_ocupado < self.disco_total:
            self.disco_ocupado += 1
            self.disco += 1024
        else:
            print 'Voce nao tem mais slots de disco disponiveis.'


if __name__ == '__main__':
    f = Fisico()
    f.contratar_cpu()
    f.contratar_memoria()
    f.contratar_memoria()
    f.contratar_disco()
    f.contratar_disco()  
    f.contratar_disco()  
    f.contratar_disco()      
    print f.cpu
    print f.memoria
    print f.disco
    f.acesso()
