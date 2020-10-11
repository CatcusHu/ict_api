import pymysql
from config.config import *

def get_db_conn():
    conn = pymysql.connect(host=db_host,port=db_port,user=db_user,password=db_passwd,db=db,charset="utf8")
    return conn
def get_db_cur():
    conn = get_db_conn()
    cur = conn.cursor()
    return cur

def close_db_conn():
    conn = get_db_conn()
    cur = get_db_cur()
    cur.close()
    return conn.close()

def alter(sql):
    conn = get_db_conn()
    cur = get_db_cur()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()

def query(sql):
    get_db_conn()
    cur = get_db_cur()
    cur.execute(sql)
    return cur.fetchall()


"""常用数控操作封装"""
def check_user(username):
    return query(f"select * from user where name='{username}'")

def add_user(username,psw):
    return query(f"insert into user (username,psw) values ('{username}','{psw}')")

def del_user(username):
    return alter(f"delete from user where name='{username}'")

# if __name__ =="__main__":
#     check_user("huxiao")