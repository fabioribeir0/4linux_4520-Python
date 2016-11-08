#!/usr/bin/python
import sys
from Modulos.Usuarios import cadastrar, remover, listar, autenticar
from Modulos.Geral import read_db, write_db
from Modulos.Servidores import add_server, rem_server, list_server


def criar_cont():
    pass


def rem_cont():
    pass


def cmd_cont():
    pass


def menu():
    print '1 - Autenticar Usuario'
    print '2 - Cadastrar Usuario'
    print '3 - Remover Usuario'
    print '4 - Listar Usuarios'
    print '5 - Adicionar Servidor'
    print '6 - Remover Servidor'
    print '7 - Listar Servidores'
    print '8 - Sair'

    try:
        opcao = input('\nSelecione uma opcao: ')
        return opcao
    except Exception as e:
        print 'Escolha um numero! ', e
        return 0


def sair():
    print 'Encerrando programa.'
    sys.exit()


def switch(x):
    funcoes = {1: autenticar,
               2: cadastrar,
               3: remover,
               4: listar,
               5: add_server,
               6: rem_server,
               7: list_server,
               8: sair}

    try:
        funcoes[x]()
    except Exception as e:
        print 'Opcao invalida. ', e

while True:
    opcao = menu()
    switch(opcao)
