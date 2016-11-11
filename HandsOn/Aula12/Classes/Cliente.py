#!/usr/bin/python
from Classes.ClienteDAO import ClienteDAO


class Cliente:

    def __init__(self, nome='', cpf='', segmento=''):
        self.nome = nome
        self.cpf = cpf
        self.segmento = segmento


    def cadastrar(self):
        self.nome = raw_input('Digite nome: ')
        self.cpf = raw_input('Digite CPF: ')
        self.segmento = raw_input('Digite o segmento: ')

        cdao = ClienteDAO()
        cdao.salvar(self)


    def buscar(self):
        self.id = raw_input('Entre com o ID do cliente: \n')
        cdao = ClienteDAO()
        cliente = cdao.busca(self.id)
        self.nome = cliente.nome
        self.cpf = cliente.cpf
        self.segmento = cliente.segmento
        return self
