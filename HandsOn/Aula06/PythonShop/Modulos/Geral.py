#!/usr/bin/python
import psycopg2 as pg


def con_db():
    con = pg.connect('host=127.0.0.1 dbname=loja user=loja password=4linux')
    cur = con.cursor()
    return cur,con


def descon_db(cur,con):
    cur.close()
    con.close()
    print 'Fechando conexao com o banco.'
