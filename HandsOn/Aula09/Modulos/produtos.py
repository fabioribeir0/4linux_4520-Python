#!/usr/bin/python
from Modulos.banco import exec_query, exec_insert


def cadastrar_produto():
    novo = {}
    novo['nome'] = raw_input('Digite o nome: ')
    novo['descricao'] = raw_input('Digite uma descricao: ')
    novo['categoria'] = raw_input('Digite a categoria: ')
    novo['preco'] = raw_input('Digite o preco: ')
    query = "insert into produtos (nome,descricao,categoria,preco) \
            values ('{0}','{1}','{2}',{3})".format(novo.get('nome'),
                                             novo.get('descricao'),
                                             novo.get('categoria'),
                                             novo.get('preco'))
    exec_insert(query)


def remover_produto():
    listar_produtos()
    pid = input('Digite o id do produto: ')
    query = 'delete from produtos where id=%s' % pid
    exec_insert(query)


def alterar_produto():
    listar_produtos()
    pid = input('Digite o id do produto: ')
    novo = {}
    novo['nome'] = raw_input('Digite o nome: ')
    novo['descricao'] = raw_input('Digite uma descricao: ')
    novo['categoria'] = raw_input('Digite a categoria: ')
    novo['preco'] = raw_input('Digite o preco: ')
    query = "update produtos set nome='{0}',descricao='{1}',\
             categoria='{2}',preco='{3}' where id='{4}'".format(
             novo.get('nome'),
             novo.get('descricao'),
             novo.get('categoria'),
             novo.get('preco'),
             pid)
    print 'QUERY: ', query
    exec_insert(query)
    


def listar_produtos():
    query = 'select * from produtos'
    produtos = exec_query(query)
    for p in produtos:
        print p
