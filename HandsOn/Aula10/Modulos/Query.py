#!/usr/bin/python
from Geral import con_db, descon_db
# from Modulos.Geral import read_db, write_db
# import json


def listar_produtos():
    cmd = 'select * from produtos;'
    cur,con = con_db()
try:
    cur.execute(cmd)
    con.commit()
    print 'Dados salvos com sucesso'

except Exception as e:
    con.rollback()
    print 'Erro ao salvar no banco.',e

finally:
    cur.close()
    con.close()


if __name__ == __main__:
    listar_produtos()
'''
def rem_cont(nome):
    cmd = 'docker stop {0} && docker rm {0}'.format(nome)
    container = main_fn(cmd)
    return container


def ip_cont(nome):
    cmd = 'docker inspect {0}'.format(nome)
    ip = main_fn(cmd)
    ip = json.loads(ip)
    ip = ip[0].get('NetworkSettings').get('IPAddress')
    return ip
'''
