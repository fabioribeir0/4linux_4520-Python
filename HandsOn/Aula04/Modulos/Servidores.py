#!/usr/bin/python
from Modulos.Geral import read_db, write_db
from Modulos.Docker import create_cont, ip_cont, rem_cont


def add_server():
    print 'Cadastrar servidor.'
    servidor = {}
    servidor['nome'] = raw_input('Digite o nome do servidor: ')
    servidor['descricao'] = raw_input('Digite uma descricao: ')

    create_cont(servidor.get('nome'))
    servidor['IP'] = ip_cont(servidor.get('nome'))

    banco = read_db()
    banco['servidores'].append(servidor)
    write_db(banco)


def rem_server():
    print 'Remover servidor.'
    servidor = raw_input('Digite o nome do servidor: ')
    banco = read_db()
    for s in banco.get('servidores'):
        if s.get('nome') == servidor:
            rem_cont(servidor)
            banco['servidores'].remove(s)
            write_db(banco)
            print 'Servidor %s removido com sucesso.' % servidor
            break
        else:
            print 'Servidor nao encontrado.'

    rem_cont(servidor)


def list_server():
    print 'Listar servidores.'
    banco = read_db()
    for i, s in enumerate(banco.get('servidores')):
        print i, '-', s.get('nome'), '-', s.get('IP')
