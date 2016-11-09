#!/usr/bin/python
import sys
from Modulos.produtos import cadastrar_produto, remover_produto, alterar_produto, listar_produtos


def menu():
    print '1 - Cadastrar Produtos'
    print '2 - Remover Produtos'
    print '3 - Alterar Produtos'
    print '4 - Listar Produtos'
    print '5 - Sair'

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
    funcoes = {1: cadastrar_produto,
               2: remover_produto,
               3: alterar_produto,
               4: listar_produtos,
               5: sair}

    try:
        funcoes[x]()
    except Exception as e:
        print 'Opcao invalida. ', e

while True:
    opcao = menu()
    switch(opcao)
