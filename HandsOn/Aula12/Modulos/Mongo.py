#!/usr/bin/python
from pymongo import MongoClient 


class Mongo:
    
    def __init__(self):
        self.client = MongoClient('127.0.0.1')
        self.db = self.client['banco_novo']


    def fila(self):
        return self.db.fila.find().count()


    def pendentes(self):
        return self.db.fila.find({'status':0})
