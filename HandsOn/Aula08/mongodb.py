#!/usr/bin/python
from pymongo import MongoClient


def conectar_banco():
    try:
        client = MongoClient('127.0.0.1')
        db = client['banco_novo']
        return db
    except Exception as e:
        print 'FALHA AO CONECTAR COM BANCO DE DADOS.\n'


def cadastrar_usuario():
    db = conectar_banco()
    novo = {}
    novo['nome'] = raw_input('Digite o nome do usuario: ')
    novo['profissao'] = raw_input('Digite a profissao do usuario: ')
    novo['skills'] = []
    novo['dependentes'] = []
    db.usuarios.insert(novo)


def listar_usuarios():
    db = conectar_banco()
    usuarios = db.usuarios.find()
    for u in usuarios:
        print '=============================='
        print 'Nome:', u.get('nome')
        print 'Profissao:', u.get('profissao')
        print 'Skills:', u.get('skills')
        print 'Endereco:', u.get('endereco')
        print '===DEPENDENTES==='
        for d in u.get('dependentes'):
            print 'Nome:', d.get('nome')
            print 'Idade:', d.get('idade')


def remover_usuario():
    db = conectar_banco()
    usuario = {}
    usuario['nome'] = raw_input('Digite o nome do usuario: ')
    db.usuarios.remove(usuario)
    print 'USUARIO REMOVIDO COM SUCESSO.\n'


def add_habilidade():
    db = conectar_banco()
    usuario = {}
    usuario['nome'] =  raw_input('Digite o nome do usuario: ')
    print 'Para sair digite #sair.'
    while True:
        skill = raw_input('Digite uma skill: ')   
        if skill == '#sair':
            break
        db.usuarios.update(usuario,{'$addToSet':{'skills':skill}})
        print 'Skill adicionada.\n'


def rem_habilidade():
    db = conectar_banco()
    usuario = {}
    usuario['nome'] =  raw_input('Digite o nome do usuario: ')
    skill = raw_input('Digite uma skill: ')   
    db.usuarios.update(usuario,{'$pull':{'skills':skill}})
    print 'Skill removida.\n'


def add_endereco():
    db = conectar_banco()
    usuario = {}
    usuario['nome'] =  raw_input('Digite o nome do usuario: ')
    endereco = {}
    endereco['rua'] = raw_input('Digite a rua: ')
    endereco['numero'] = raw_input('Digite o numero: ')
    endereco['cidade'] = raw_input('Digite a cidade: ')
    db.usuarios.update(usuario,{'$set':{'endereco':endereco}})


def add_dependente():
    db = conectar_banco()
    usuario = {}
    usuario['nome'] =  raw_input('Digite o nome do usuario: ')
    dependente = {}
    dependente['nome'] = raw_input('Digite o nome do dependente: ')
    dependente['idade'] = input('Digite a idade: ')
    db.usuarios.update(usuario,{'$addToSet':{'dependentes':dependente}})
    print 'Adicionado com sucesso.'


def atualizar_dependente():
    db = conectar_banco()
    usuario = {}
    usuario['nome'] =  raw_input('Digite o nome do usuario: ')
    dependente = {}
    dependente['nome'] = raw_input('Digite o nome do dependente: ')
    dependente['idade'] = input('Digite a idade: ')
    
    criterio = {'nome':usuario.get('nome'),'dependentes.nome'
               :dependente.get('nome')}

    update = {'$set':{'dependentes.$.idade':dependente.get('idade')}}

    db.usuarios.update(criterio, update)
    print 'Adicionado com sucesso.'


def switch(x):
    funcoes = {1:cadastrar_usuario,
               2:remover_usuario,
               3:listar_usuarios,
               4:add_habilidade,
               5:rem_habilidade,
               6:add_endereco,
               7:add_dependente,
               8:atualizar_dependente}
    funcoes[x]()


if __name__ == '__main__':
    print '1 - Cadastrar'
    print '2 - Remover'
    print '3 - Listar'
    print '4 - Add Skills'
    print '5 - Rem Skill'
    print '6 - Add Endereco'
    print '7 - Add dependente'
    print '8 - Atualizar dependente'
    op = input('Selecione uma opcao: ')
    switch(op)
