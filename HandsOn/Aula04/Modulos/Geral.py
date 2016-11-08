#!/usr/bin/python
import json


def read_db():
    with open('banco.json', 'r') as f:
        # o arquivo lido e do tipo str
        arquivo = f.read()
        arquivo = json.loads(arquivo)
    return arquivo


def write_db(dic):
    with open('banco.json', 'w') as f:
        arquivo = json.dumps(dic)
        f.write(arquivo)
