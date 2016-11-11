#!/usr/bin/python
from Model.Model import Servico, Cliente, Produto, session


class ServicoDAO:

    def salvar(self, servico):
        cliente = session.query(Cliente)\
                  .filter(Cliente.id==servico.cliente).first()
        produto = session.query(Produto)\
                  .filter(Produto.id==servico.produto).first()
        try:
            s = Servico()
            s.produto_id = produto.id
            cliente.servico.append(s)
            session.add(s)
            session.commit()
            print '==SERVICO CADASTRADO COM SUCESSO=='
        except Exception as e:
            session.rollback()
            print '==FALHA AO CADASTRAR SERVICO==\n%s' % e


    def buscar(self, id):
        try:
            servico = session.query(Servico,Cliente,Produto)\
                      .filter(Servico.id==id)\
                      .join(Cliente).join(Produto).first()
            return servico
        except Exception as e:
            print '==FALHOU AO BUSCAR SERVICO==\n%s' % e
