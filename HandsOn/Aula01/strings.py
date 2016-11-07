#!/usr/bin/python

nome = 'Guido'
idade = 59

print 'Criador do Python: ' + nome
print 'Idade:', idade

texto = ''
texto += 'Criador do Python: '
texto += nome
texto += '\nIdade: %s' %idade

print texto

print 'Criador do Python: %s\nIdade: %s'%(nome,idade)

print 'Criador do Python: {}\nIdade: {}'.format(nome,idade)
