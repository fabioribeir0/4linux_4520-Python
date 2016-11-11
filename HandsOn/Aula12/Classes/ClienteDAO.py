#!/usr/bin/python
from Model.Model import session, Cliente as ClienteModel


class ClienteDAO:

    def salvar(self, cliente):
        try:
            novo = ClienteModel(cliente)
            session.add(novo)
            session.commit()
            print '==CLIENTE SALVO COM SUCESSO==\n'
        except Exception as e:
            session.rollback()
            print '==FALHOU AO CADASTRAR USUARIO==\n%s' % e


    def busca(self, id):
        try:
            cliente = session.query(ClienteModel)\
                      .filter(ClienteModel.id==id).first()
            return cliente
        except Exception as e:
            print '==FALHOU AO BUSCAR USUARIO==%s\n' % e
