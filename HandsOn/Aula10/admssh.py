#!/usr/bin/python
import sys
from Modulos.Usuarios import Usuarios
from Modulos.Servidores import Servidores


class AdmSSH:


    def menu(self):
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


    def sair(self):
        print 'Encerrando programa.'
        sys.exit()


    def switch(self, x):
        u = Usuarios()
        s = Servidores()
        funcoes = {1: u.autenticar,
                   2: u.cadastrar,
                   3: u.remover,
                   4: u.listar,
                   5: s.cadastrar,
                   6: s.remover,
                   7: s.listar,
                   8: self.sair}

        try:
            funcoes[x]()
        except Exception as e:
            print 'Opcao invalida. ', e


if __name__ == '__main__':
    admssh = AdmSSH()
    while True:
        opcao = admssh.menu()
        admssh.switch(opcao)
