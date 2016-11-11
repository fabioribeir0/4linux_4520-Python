#!/usr/bin/python
from Classes.Servico import Servico
from Modulos.Docker import Docker


class Provisionar:

    def start(self, sid):
        s = Servico()
        servico = s.buscar(sid)
        print 'ID do servico:', servico.id
        print 'Contratante:', servico.cliente.nome
        print 'Produto:', servico.produto.nome
        print 'Data:', servico.data

        d = Docker()
        d.criar(servico.produto.nome, servico.produto.imagem)
        print 'Servico provicionado.'
