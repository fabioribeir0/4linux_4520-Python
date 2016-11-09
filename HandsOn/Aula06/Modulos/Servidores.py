#!/usr/bin/python
from Modulos.banco import exec_insert, exec_query
from Modulos.Docker import create_cont, ip_cont, rem_cont


def cadastrar_servidor():
    print 'Cadastrar servidor.'
    servidor = {}
    servidor['nome'] = raw_input('Digite o nome do servidor: ')
    servidor['descricao'] = raw_input('Digite uma descricao: ')

    create_cont(servidor.get('nome'))
    servidor['ip'] = ip_cont(servidor.get('nome'))

    query = "insert into servidores (nome,descricao,ip) \
            values ('{0}','{1}','{2}')".format(servidor.get('nome'),
                                               servidor.get('descricao'),
                                               servidor.get('ip'))
    exec_insert(query)
    print 'Dados gravados com sucesso.'


def remover_servidor():
    listar_servidores()
    sid = input('Digite o id do servidor: ')
    query = 'select * from servidores where id={0}'.format(sid)
    servidor = exec_query(query)
    servidor = servidor[0][1]
    print 'Apagando servidor.'
    rem_cont(servidor)
    query = 'delete from servidores where id={0}'.format(sid)
    exec_insert(query)




def listar_servidores():
    query = 'select * from servidores'
    servidores = exec_query(query)
    for s in servidores:
        print s
