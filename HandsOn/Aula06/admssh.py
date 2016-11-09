#!/usr/bin/python
import sys
from Modulos.Usuarios import cadastrar_usuario, remover_usuario, listar_usuarios, autenticar_usuario
from Modulos.Servidores import cadastrar_servidor, remover_servidor, listar_servidores


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
    funcoes = {1: autenticar_usuario,
               2: cadastrar_usuario,
               3: remover_usuario,
               4: listar_usuarios,
               5: cadastrar_servidor,
               6: remover_servidor,
               7: listar_servidores,
               8: sair}

    try:
        funcoes[x]()
    except Exception as e:
        print 'Opcao invalida. ', e

while True:
    opcao = menu()
    switch(opcao)
