#!/usr/bin/python
from Modulos.model import session, Usuarios as UsuariosModel, Tokens


class Usuarios:


    def cadastrar(self):
        print 'CADASTRAR USUARIO.\n'    
        self.login = raw_input('Digite o login do usuario: ')
        self.senha = raw_input('Digite a senha do usuario: ')
        try:
            novo = UsuariosModel(self)
            session.add(novo)
            session.commit()
            print 'USUARIO CADASTRADO COM SUCESSO!\n'
        except Exception as e:
            session.rollback()
            print 'FALHA AO CADASTRAR O USUARIO:', e


    def remover(self):
        self.listar()
        uid = input('Digite o id do usuario: ')
        usuario = session.query(UsuariosModel)\
                  .filter(UsuariosModel.id==uid).first()
        try:
            session.delete(usuario)
            session.commit()
        except Exception as e:
            session.rollback()
            print 'FALHA AO REMOVER USUARIO.', e


    def listar(self):
        print 'LISTAR USUARIOS.\n'
        usuarios = session.query(UsuariosModel).all()
        for u in usuarios:
            print u.id, '-', u.login
        print '\n'


    def autenticar(self):
        print 'AUTENTICAR!\n'
        self.login = raw_input('Digite o login do usuario: ')
        self.senha = raw_input('Digite a senha do usuario: ')
        usuario = session.query(UsuariosModel)\
                  .filter(UsuariosModel.login==self.login,\
                  UsuariosModel.senha==self.senha).first()
        if usuario:
            t = Tokens()
            usuario.tokens.append(t)
            session.add(t)
            session.commit()
            print 'USUARIO AUTENTICADO COM SUCESSO!\n'
            print 'TOKEN DE ACESSO:', t.token, '\n'
        else:
            print 'USUARIO OU SENHA INVALIDA!\n'
