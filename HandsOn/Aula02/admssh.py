#!/usr/bin/python
import sys
import json


def criar_cont():
    pass


def rem_cont():
    pass


def cmd_cont():
    pass


def menu():
    print '1 - Cadastrar'
    print '2 - Remover'
    print '3 - Listar'
    print '4 - Autenticar'
    print '5 - Criar Container'
    print '6 - Remover Container'
    print '7 - Executar comando'
    print '8 - Sair'
    
    try:
        opcao = input('\nSelecione uma opcao: ')
        return opcao
    except Exception as e:
        print 'Escolha um numero! ', e
        return 0


def read_db():
    with open('banco.json', 'r') as f:
        #o arquivo lido e do tipo str        
        arquivo = f.read()
        arquivo = json.loads(arquivo)
    return arquivo


def write_db(dic):
    with open('banco.json', 'w') as f:
        arquivo = json.dumps(dic)
        f.write(arquivo)


def cadastrar():
    print 'Cadastrar usuario.'
    novo = {}
    novo['login'] = raw_input('Digite o login do usuario: ')
    #{'login': 'fabio'}
    novo['senha'] = raw_input('Digite a senha do usuario: ')
    #{'login': 'fabio', 'senha': '1234'}    
    print 'Usuario %s cadastrado com sucesso' %novo['login']
    
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
            print 'Usuario %s removido com sucesso.' %usuario
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
    senha = raw_input('Digite sua senha:')

    for u in content.get('usuarios'):
        if u.get('login') == user and u.get('senha') == senha:
            print 'Login efetuado com sucesso.'
            break
    else:
        print 'Usuario ou senha invalida.'


def sair():
    print 'Encerrando programa.'
    sys.exit()


def switch(x):
    funcoes = {1:cadastrar,
               2:remover,
               3:listar,
               4:autenticar,
               5:criar_cont,
               6:rem_cont,
               7:cmd_cont,
               8:sair}
    
    try:
        funcoes[x]()
    except Exception as e:
        print 'Opcao invalida. ', e

while True:
    opcao = menu()
    switch(opcao)
