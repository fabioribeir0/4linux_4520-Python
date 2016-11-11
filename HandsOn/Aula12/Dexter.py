#!/usr/bin/python
from Classes.Produto import Produto
from Classes.Cliente import Cliente
from Classes.Servico import Servico


print '1 - Cadastrar cliente'
print '2 - Cadastrar produto'
print '3 - Buscar cliente'
print '4 - Buscar produto'
print '5 - Cadastrar servico'
print '6 - Buscar servico'


p = Produto()
c = Cliente()
s = Servico()

op = input('Digite uma opcao: ')
if op == 1:
    c.cadastrar()
elif op == 2:
    p.cadastrar()
elif op == 3:
    c.buscar()
elif op == 4:
    p.buscar()
elif op == 5:
    s.cadastrar()
elif op == 6:
    servico = s.buscar()
    print 'ID:', servico.id
    print 'Cliente:', servico.cliente.nome
    print 'Produto:', servico.produto.nome
    print 'Data:', servico.data
