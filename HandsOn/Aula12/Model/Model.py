#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from random import randint
from datetime import datetime


# definir banco

# engine = create_engine('sqlite:///banco.db')
engine = create_engine('mysql://root:123456@127.0.0.1/admssh')
# cria objeto sessionmaker
Session = sessionmaker()
# define qual banco a sessao vai ouvir
Session.configure(bind=engine)
# abre sessao para ser usada
session = Session()

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(50))
    cpf = Column(String(50))
    segmento = Column(String(50))
    servico = relationship('Servico')


    def __init__(self,cliente=''):
        self.nome = cliente.nome
        self.cpf = cliente.cpf
        self.segmento = cliente.segmento


class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(20))
    descricao = Column(String(20))
    imagem = Column(String(50))


    def __init__(self,produto=''):
        self.nome = produto.nome
        self.descricao = produto.descricao
        self.imagem = produto.imagem


class Servico(Base):
    __tablename__ = 'servico'
    id = Column(Integer, primary_key=True, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    produto_id = Column(Integer, ForeignKey('produto.id'))
    data = Column(DateTime, default=datetime.now())
    produto = relationship('Produto')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    c = Cliente()
    c.nome = 'Joao'
    c.cpf = '30130130120'
    c.segmento = 'TI'
    session.add(c)

    p = Produto()
    p.nome = 'Backup'
    p.descricao = 'Servidor de Backup'
    p.imagem = 'ubuntu'
    session.add(p)

    cliente = session.query(Cliente).filter(Cliente.nome=='Joao').first()
    produto = session.query(Produto).filter(Produto.nome=='Backup').first()

    s = Servico()
    s.produto_id = produto.id
    cliente.servico.append(s)

    session.add(s)
    session.commit()
