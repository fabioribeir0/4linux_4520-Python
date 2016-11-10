#!/usr/bin/python


class Produtos:


    def __init__(self, nome='', descricao='', categoria='', preco=0):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.__quantidade = 10


    def __str__(self):
        texto = ''
        texto += 'Nome: %s\n' % self.nome
        texto += 'Descricao: %s\n' % self.descricao
        texto += 'Categoria: %s\n' % self.categoria
        texto += 'Preco: %s' % self.preco
        return texto


    def vender(self):
        self.quantidade -= 1
        print 'Quantidade em estoque:', self.quantidade


if __name__ == '__main__':
    p = Produtos('Monitor','LG','Informatica',100)
    print p
    p.vender
