#!/usr/bin/python
from Modulos.Mongo import Mongo
from Classes.Provisionar import Provisionar

class Daemon:
    def main(self):
        m = Mongo()
        prov = Provisionar()
        print 'Servicos na fila:', m.fila()
        print 'Pendentes:', m.pendentes().count()
        for p in m.pendentes():
            print p
            prov.start(p.get('servico'))
            


if __name__ == '__main__':
    d = Daemon()
    d.main()
