#!/usr/bin/python
import psycopg2 as pg
import MySQLdb as sql


def con_db():
    try:
        if 'mysql':
            con = sql.connect(host='127.0.0.1',db='loja',
                  user='root',passwd='123456')
        else:
            con = pg.connect('host=127.0.0.1 dbname=loja user=loja \
                  password=4linux')
            
        cur = con.cursor()
        return (con,cur)
    except Exception as e:
        print 'Erro:', e
        

def exec_query(query):
    con, cur = con_db()
    try:
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print 'Erro:', e
    finally:
        cur.close()
        con.close()


def exec_insert(query):
    con, cur = con_db()
    try:
        cur.execute(query)
        con.commit()
        print 'Dado gravado com sucesso.'
    except Exception as e:
        con.rollback()
        print 'Erro:', e
    finally:
        cur.close()
        con.close()
