#!/usr/bin/python
import MySQLdb as sql


def con_db():
    try:
        con = sql.connect(host='127.0.0.1',db='admssh',
              user='root',passwd='123456')
        cur = con.cursor()
        return (con,cur)
    except Exception as e:
        print 'Erro de conexao ao servidor:', e
        

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
