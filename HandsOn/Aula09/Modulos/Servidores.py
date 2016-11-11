#!/usr/bin/python
from Modulos.model import session, Servidores as ServidoresModel, Tokens
from Modulos.Docker import Docker
from datetime import datetime


class Servidores:


    def __init__(self):
        self.docker = Docker()


    def cadastrar(self):
        t = input('Digite seu token de acesso: ')
        acesso = session.query(Tokens).filter(Tokens.token==t).first()
        if not acesso or (datetime.now() -\
                         acesso.data).total_seconds() > 3600:
            print 'TOKEN INVALIDO OU EXPIRADO!\n'
            return
        print 'CADASTRAR SERVIDOR.\n'

        self.name = raw_input('Digite o nome do servidor: ')
        self.descricao = raw_input('Digite uma descricao: ')

        self.docker.create(self.name)
        self.ip = self.docker.ip(self.name)

        try:
            servidor = ServidoresModel(self)
            session.add(servidor)
            s = session.query(ServidoresModel).filter(ServidoresModel.name==
                self.name).first()
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


    def remover(self):
        self.listar()
        sid = input('Digite o id do servidor: ')
        servidor = session.query(ServidoresModel)\
                   .filter(ServidoresModel.id==sid).first()
        print 'APAGANDO SERVIDOR.\n'
        self.docker.rem(servidor.name)
        try:
            t = session.query(Tokens)\
                .filter(Tokens.servidores_id==servidor.id)\
                .first()
            session.delete(t)
            session.delete(servidor)
            session.commit()
            print 'SERVIDOR REMOVIDO COM SUCESSO.\n'
        except Exception as e:
            session.rollback()
            print 'FALHA AO REMOVER SERVIDOR: %s\n' % e


    def listar(self):
        print 'LISTAR SERVIDORES.\n'
        servidores = session.query(ServidoresModel).all()
        for s in servidores:
            print s.id, '-', s.name, ',', s.ip
        print '\n'
