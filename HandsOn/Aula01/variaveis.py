#!/usr/bin/python

PI = 3.14
cep = 11700250
preco = 19.90
nome = 'sapato'
lista = ['tenis', 'sapato', 'sandalia', 'chinelo']
tupla = ('tenis', 'sapato', 'sandalia', 'chinelo')
dic = {'produto': 'TV', 'produto1': 'DVD', 'produto2': 'Rack'}

print 'Exibindo variaveis:\n', PI, cep, preco, nome, '\n'

print 'Estrutura de dados:\n'
print 'Lista:', lista, lista[0], '\n'
print 'Tupla:', tupla, tupla[2], '\n'
print 'Dicionario:', dic, dic.get('produto'), dic.get('produto1')

dic['produto'] = 'video-game'
print 'Novo produto', dic.get('produto')
