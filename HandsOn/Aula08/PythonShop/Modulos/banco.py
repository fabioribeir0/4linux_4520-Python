#!/usr/bin/python
from pymongo import MongoClient


def conectar_banco():
    try:
        client = MongoClient('127.0.0.1')
        db = client['banco_novo']
        return db
    except Exception as e:
        print 'FALHA AO CONECTAR COM BANCO DE DADOS.\n'
        

def exec_find(criterio={}):
    db = conectar_banco()
    return db.produtos.find(criterio)


def exec_insert(dados):
    db = conectar_banco()
    db.produtos.insert(dados)


def exec_remove(criterio):
    db = conectar_banco()
    db.produtos.remove(criterio)


def exec_update(criterio, dados):
    db = conectar_banco()
    db.produtos.update(criterio,{'$set':dados})
