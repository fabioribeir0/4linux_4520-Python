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


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String(20))
    senha = Column(String(20))
    tokens = relationship('Tokens')


class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20))
    descricao = Column(String(20))
    ip = Column(String(20))


class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, nullable=False)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    servidores_id = Column(Integer, ForeignKey('servidores.id'))
    token = Column(String(20), default=randint(1000,9999))
    data = Column(DateTime, default=datetime.now())
    servidores = relationship('Servidores')
    usuarios = relationship('Usuarios')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    token = Tokens()
    u = session.query(Usuarios).filter(Usuarios.id==1).first()
    u.tokens.append(token)
    s = Servidores()
    s.nome = 'Novo Servidor'
    s.ip = '172.17.0.2'
    session.add(s)
    s = session.query(Servidores).filter(Servidores.id==1).first()
    token.servidores_id = s.id
    session.add(token)
    session.commit()
#    novo = Usuarios()
#    novo.login = 'fabio.ribeiro'
#    novo.senha = '4linux'
#    session.add(novo)
#    session.commit()
#    u = session.query(Usuarios).filter(Usuarios.login=='fabio.ribeiro')\
#        .first()
#    u.login = 'fabio.ribeiro'
#    session.commit()
#    todos = session.query(Usuarios).all()
#    for u in todos:
#        # print u.__dict__
#        print u.login, u.senha
