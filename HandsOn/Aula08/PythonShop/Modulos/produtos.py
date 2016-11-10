#!/usr/bin/python
from Modulos.banco import exec_find, exec_insert, exec_remove, exec_update


def cadastrar_produto():
    novo = {}
    novo['nome'] = raw_input('Digite o nome: ')
    novo['descricao'] = raw_input('Digite uma descricao: ')
    novo['categoria'] = raw_input('Digite a categoria: ')
    novo['preco'] = raw_input('Digite o preco: ')
    exec_insert(novo)
    print 'Produto cadastrado.\n'


def remover_produto():
    listar_produtos()
    nome = raw_input('Digite o nome do produto: ')
    exec_remove({'nome':nome})
    print 'PRODUTO REMOVIDO COM SUCESSO.\n'


def alterar_produto():
    listar_produtos()

    nome = raw_input('Digite o nome do produto a ser alterado: ')
    print 'Digite as novas informacoes:\n'
    novo = {}
    novo['nome'] = raw_input('Digite o nome: ')
    novo['descricao'] = raw_input('Digite uma descricao: ')
    novo['categoria'] = raw_input('Digite uma categoria: ')
    novo['preco'] = raw_input('Digite o preco: ')
    exec_update({'nome':nome},novo)
    print 'Alterado com sucesso.'


def listar_produtos():
    produtos = exec_find()
    for p in produtos:
        print p
