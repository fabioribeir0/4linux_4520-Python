#!/usr/bin/python

for i in range(0,20,2):
    print i

produtos = ['tenis', 'chinelo', 'tv', 'computador']
for p in produtos:
    print p

for i,p in enumerate(produtos):
    print i, '-', p


dic = {'produto1': 'TV', 'produto2': 'Xbox', 'produto3': 'PS4'}

for p in dic:
    print p, '-', dic.get(p)
    print dic[p]


servidores = ['ldap', 'apache', 'mysql', 'redis', 'docker']

for s in servidores:
    if s == 'redis':
        continue
    print s, 'em manutencao.'
