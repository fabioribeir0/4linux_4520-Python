#!/usr/bin/python

usuarios = ['marvin', 'arthur', 'ford', 'fabio']
senhas = ['senha123', 'ath123', 'xxx', '1234']

print 'AUTENTICACAO\n'

user = raw_input('Digite seu login: ')

for u in usuarios:
    if u == user:
        senha = raw_input('Digite sua senha:')
        if senha == senhas[usuarios.index(u)]:
            print 'Login efetuado com sucesso.'
            break
else:
    print 'Usuario ou senha invalida.'
