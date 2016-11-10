#!/usr/bin/python
from Modulos.banco import exec_query, exec_insert
from pymongo import MongoClient


def conectar_banco():
    try:
        client = MongoClient('127.0.0.1')
        db = client['banco_novo']
        return db
    except Exception as e:
        print 'FALHA AO CONECTAR COM BANCO DE DADOS.\n'


def cadastrar_produto():
    db = conectar_banco()
    novo = {}
    novo['nome'] = raw_input('Digite o nome: ')
    novo['descricao'] = raw_input('Digite uma descricao: ')
    novo['categoria'] = raw_input('Digite a categoria: ')
    novo['preco'] = raw_input('Digite o preco: ')
    db.produtos.insert(novo)


def remover_produto():
    db = conectar_banco()
    listar_produtos()
    produto = {}
    produto['nome'] = raw_input('Digite o nome do produto: ')
    db.produtos.remove(produto)
    print 'PRODUTO REMOVIDO COM SUCESSO.\n'


def alterar_produto():
    db = conectar_banco()
    listar_produtos()
    novo = {}
    novo['nome'] =  raw_input('Digite o nome do produto: ')
    
    novo['nome'] = raw_input('Digite o nome: ')
    novo['descricao'] = raw_input('Digite uma descricao: ')
    novo['categoria'] = raw_input('Digite a categoria: ')
    novo['preco'] = raw_input('Digite o preco: ')
    produto = {}
    dependente['nome'] = raw_input('Digite o nome do dependente: ')
    dependente['idade'] = input('Digite a idade: ')
    
    criterio = {'nome':usuario.get('nome'),'dependentes.nome'
               :dependente.get('nome')}

    update = {'$set':{'dependentes.$.idade':dependente.get('idade')}}

    db.usuarios.update(criterio, update)
    print 'Adicionado com sucesso.'
    


def listar_produtos():
    db = conectar_banco()
    produtos = db.produtos.find()
    for p in produtos:
        print '=============================='
        print 'Nome:', p.get('nome')
        print 'Descricao:', p.get('descricao')
        print 'Categoria:', p.get('categoria')
        print 'Preco:', p.get('preco')
