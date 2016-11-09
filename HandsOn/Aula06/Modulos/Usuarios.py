#!/usr/bin/python
from Modulos.banco import exec_insert, exec_query


def cadastrar_usuario():
    print 'Cadastrar usuario.'
    novo = {}
    novo['login'] = raw_input('Digite o login do usuario: ')
    novo['senha'] = raw_input('Digite a senha do usuario: ')

    query = "insert into usuarios (login,senha) \
            values ('{0}','{1}')".format(novo.get('login'),
                                         novo.get('senha'))
    exec_insert(query)
    print 'Usuario cadastrado com sucesso!'


def remover_usuario():
    listar_usuarios()
    uid = input('Digite o id do usuario: ')
    query = 'delete from usuarios where id={}'.format(uid)
    exec_insert(query)



def listar_usuarios():
    print 'Listar usuarios.'
    query = 'select * from usuarios'
    usuarios = exec_query(query)
    for u in usuarios:
        print u


def autenticar_usuario():
    print 'Autenticar!'
    usuario = raw_input('Digite o login do usuario: ')
    senha = raw_input('Digite a senha do usuario: ')
    query = "select * from usuarios where login='{0}' and senha='{1}'"\
            .format(usuario,senha)
    usuario = exec_query(query)

    if usuario:
        print 'Usuario autenticado com sucesso'
    else:
        print 'Usuario ou senha invalida'
