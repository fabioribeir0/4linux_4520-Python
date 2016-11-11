#!/usr/bin/python
from Classes.ServicoDAO import ServicoDAO
from Classes.Cliente import Cliente
from Classes.Produto import Produto


class Servico:

    def cadastrar(self):
        self.cliente = raw_input('Digite o ID do cliente: ')
        self.produto = raw_input('Digite o ID do produto: ')
        sdao = ServicoDAO()
        sdao.salvar(self)


    def buscar(self, id):
        self.id = id
        sdao = ServicoDAO()
        servico = sdao.buscar(self.id)

        c = Cliente(servico.Cliente.nome,servico.Cliente.cpf,
                    servico.Cliente.segmento)
        p = Produto(servico.Produto.nome,servico.Produto.descricao,
                    servico.Produto.imagem)

        self.cliente = c
        self.produto = p
        self.data = servico.Servico.data
        return self
