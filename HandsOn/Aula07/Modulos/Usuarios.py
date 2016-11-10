#!/usr/bin/python
from Modulos.model import session, Usuarios, Tokens


def cadastrar_usuario():
    print 'CADASTRAR USUARIO.\n'    
    novo = Usuarios()
    novo.login = raw_input('Digite o login do usuario: ')
    novo.senha = raw_input('Digite a senha do usuario: ')
    try:
        session.add(novo)
        session.commit()
        print 'USUARIO CADASTRADO COM SUCESSO!\n'
    except Exception as e:
        session.rollback()
        print 'FALHA AO CADASTRAR O USUARIO:', e


def remover_usuario():
    listar_usuarios()
    uid = input('Digite o id do usuario: ')
    usuario = session.query(Usuarios).filter(Usuarios.id==uid).first()
    try:
        session.delete(usuario)
        session.commit()
    except Exception as e:
        session.rollback()
        print 'FALHA AO REMOVER USUARIO.', e


def listar_usuarios():
    print 'LISTAR USUARIOS.\n'
    usuarios = session.query(Usuarios).all()
    for u in usuarios:
        print u.id, '-', u.login
    print '\n'


def autenticar_usuario():
    print 'AUTENTICAR!\n'
    login = raw_input('Digite o login do usuario: ')
    senha = raw_input('Digite a senha do usuario: ')
    usuario = session.query(Usuarios).filter(Usuarios.login==login,
                                             Usuarios.senha==senha).first()
    if usuario:
        t = Tokens()
        usuario.tokens.append(t)
        session.add(t)
        session.commit()
        print 'USUARIO AUTENTICADO COM SUCESSO!\n'
        print 'TOKEN DE ACESSO:', t.token, '\n'
    else:
        print 'USUARIO OU SENHA INVALIDA!\n'
