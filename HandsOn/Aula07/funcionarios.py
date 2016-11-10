#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

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


class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(20))
    dependentes = relationship('Dependentes')


class Dependentes(Base):
    __tablename__ = 'dependentes'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(20))
    funcionarios_id = Column(Integer,ForeignKey('funcionarios.id'))


if __name__=='__main__':
    Base.metadata.create_all(engine)
    joaquim = session.query(Funcionarios)\
                     .filter(Funcionarios.nome=='Joaquim Teixeira')\
                     .first()

#    for dependente in joaquim.dependentes:
#        print dependente.nome
    novo = Dependentes()
    novo.nome = 'Jose Teixeira'
    joaquim.dependentes.append(novo)
    
#    novo = Funcionarios()
#    novo.nome = 'Joaquim Teixeira'
    session.add(novo)
    session.commit()
