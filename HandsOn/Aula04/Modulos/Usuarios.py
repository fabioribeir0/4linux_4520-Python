#!/usr/bin/python
from Modulos.Geral import read_db, write_db


def cadastrar():
    print 'Cadastrar usuario.'
    novo = {}
    novo['login'] = raw_input('Digite o login do usuario: ')
    # {'login': 'fabio'}
    novo['senha'] = raw_input('Digite a senha do usuario: ')
    # {'login': 'fabio', 'senha': '1234'}
    print 'Usuario %s cadastrado com sucesso' % novo['login']

    content = read_db()
    content['usuarios'].append(novo)

    write_db(content)

    print 'Saindo...\n'


def remover():
    print 'Remover usuario.'
    usuario = raw_input('Digite o login do usuario: ')
    content = read_db()
    for u in content.get('usuarios'):
        if u.get('login') == usuario:
            content['usuarios'].remove(u)
            write_db(content)
            print 'Usuario %s removido com sucesso.' % usuario
            break
        else:
            print 'Usuario nao encontrado.'


def listar():
    print 'Listar usuarios.'
    content = read_db()
    for u in content.get('usuarios'):
        print u


def autenticar():
    print 'Autenticar usuario.\n'
    content = read_db()
    user = raw_input('Digite seu login: ')
    senha = raw_input('Digite sua senha: ')

    for u in content.get('usuarios'):
        if u.get('login') == user and u.get('senha') == senha:
            print 'Login efetuado com sucesso.'
            break
    else:
        print 'Usuario ou senha invalida.'
