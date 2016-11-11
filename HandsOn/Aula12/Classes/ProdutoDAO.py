#!/usr/bin/python
from Model.Model import Produto, session


class ProdutoDAO:

    def salvar(self, produto):
        try:
            p = Produto(produto)
            session.add(p)
            session.commit()
            print '==PRODUTO CADASTRADO COM SUCESSO==\n'
        except Exception as e:
            session.rollback()
            print '==FALHOU AO SALVAR PRODUTO==\n%s' % e


    def busca(self, id):
        try:
            produto = session.query(Produto).filter(Produto.id==id).first()
            return produto
        except Exception as e:
            session.rollback()
            print '==FALHOU AO BUSCAR PRODUTO==\n%s' % e

