#!/usr/bin/python
from Classes.ProdutoDAO import ProdutoDAO


class Produto:

    def __init__(self, nome='', descricao='', imagem=''):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem


    def cadastrar(self):
        self.nome = raw_input('Digite o nome: \n')
        self.descricao = raw_input('Digite a descricao: \n')
        self.imagem = raw_input('Imagem: \n')

        pdao = ProdutoDAO()
        pdao.salvar(self)


    def buscar(self):
        self.id = raw_input('Digite o ID do produto: \n')
        pdao = ProdutoDAO()
        produto = pdao.busca(self.id)
        self.nome = produto.nome
        self.descricao = produto.descricao
        self.imagem = produto.imagem
        return self
