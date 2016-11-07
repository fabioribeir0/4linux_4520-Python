#!/usr/bin/python

saldo = 0
valor = input('Digite o valor: ')

saldo += valor

while saldo < 0:
    print 'Saldo atual', saldo, '\nJuros serao cobrados.'
    valor = input('Valor do deposito: ')
    saldo += valor
