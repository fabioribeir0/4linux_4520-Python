#!/usr/bin/python
from Modulos.model import session, Servidores
from Modulos.Docker import create_cont, rem_cont, ip_cont


def cadastrar_servidor():
    print 'CADASTRAR SERVIDOR.\n'
    servidor = Servidores()
    servidor.name = raw_input('Digite o nome do servidor: ')
    servidor.descricao = raw_input('Digite uma descricao: ')

    create_cont(servidor.name)
    servidor.ip = ip_cont(servidor.name)

    try:
        session.add(servidor)
        session.commit()
        print 'SERVIDOR CADASTRADO COM SUCESSO!\n'
    except Exception as e:
        session.rollback()
        print 'FALHA AO CADASTRAR O SERVIDOR:', e


def remover_servidor():
    listar_servidores()
    sid = input('Digite o id do servidor: ')
    servidor = session.query(Servidores).filter(Servidores.id==sid).first()
    print 'APAGANDO SERVIDOR.\n'
    rem_cont(servidor.name)
    try:
        session.delete(servidor)
        session.commit()
        print 'SERVIDOR REMOVIDO COM SUCESSO.\n'
    except Exception as e:
        session.rollback()
        print 'FALHA AO REMOVER SERVIDOR.', e


def listar_servidores():
    print 'LISTAR SERVIDORES.\n'
    servidores = session.query(Servidores).all()
    for s in servidores:
        print s.id, '-', s.name, ',', s.ip
    print '\n'
