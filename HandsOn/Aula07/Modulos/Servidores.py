#!/usr/bin/python
from Modulos.model import session, Servidores, Tokens
from Modulos.Docker import create_cont, rem_cont, ip_cont
from datetime import datetime

def cadastrar_servidor():
    t = input('Digite seu token de acesso: ')
    acesso = session.query(Tokens).filter(Tokens.token==t).first()
    if not acesso or (datetime.now() - acesso.data).total_seconds() > 3600:
        print 'TOKEN INVALIDO OU EXPIRADO!\n'
        return
    print 'CADASTRAR SERVIDOR.\n'
    servidor = Servidores()
    servidor.name = raw_input('Digite o nome do servidor: ')
    servidor.descricao = raw_input('Digite uma descricao: ')

    create_cont(servidor.name)
    servidor.ip = ip_cont(servidor.name)

    try:
        session.add(servidor)
        s = session.query(Servidores).filter(Servidores.name==
            servidor.name).first()
        t = Tokens()
        t.token = acesso.token
        t.data = acesso.data
        t.usuarios_id = acesso.usuarios_id
        t.servidores_id = s.id
        session.add(t)
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
        t = session.query(Tokens).filter(Tokens.servidores_id==servidor.id)\
            .first()
        session.delete(t)
        session.delete(servidor)
        session.commit()
        print 'SERVIDOR REMOVIDO COM SUCESSO.\n'
    except Exception as e:
        session.rollback()
        print 'FALHA AO REMOVER SERVIDOR.', e, '\n'


def listar_servidores():
    print 'LISTAR SERVIDORES.\n'
    servidores = session.query(Servidores).all()
    for s in servidores:
        print s.id, '-', s.name, ',', s.ip
    print '\n'
