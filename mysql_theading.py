# -*- coding: utf-8 -*-
# author: itimor
# 多线程插入sql

import pymysql as MySQLdb
import threading

class MYSQL:
    def __init__(self, db):
        self.conn = MySQLdb.connect(
            host=db["host"],
            port=db["port"],
            user=db["user"],
            passwd=db["passwd"],
            db=db["db"],
            charset='utf8')
        self.cursor = self.conn.cursor()

    def insert(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return True

    def select(self,sql):
        self.cursor.execute(sql)
        alldata = self.cursor.fetchall()
        return alldata

    def update(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return True

    def close(self):
        self.cursor.close()
        self.conn.close()


def batch_sql_insert():
    jobapi = MYSQL(xxljob_info)
    try:
      for i in range(1):
        print(i)
        sql = f"INSERT INTO `canal_manager_test`.`es_suggest_key` (`keyword`,`keyword_type`,`weight`) VALUES ('aaa',{i},{i});"
        jobapi.insert(sql)
    except Exception as e:
        print ("one error happen",e)
    finally:
        jobapi.close()

class myThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        pass
    def run(self):
        batch_sql_insert()
        #print ("开始操作%s"%i)


if __name__ == '__main__':
    xxljob_info = {
        "host": "172.31.250.114",
        "port": 3306,
        "user": "canal",
        "passwd": "canal",
        "db": "canal_manager_test",
    }
    threads =[]
    tlock=threading.Lock()
    for  i in range(100):
        thread = myThread(i)
        threads.append(thread)
    
    for i in range(len(threads)):
        threads[i].start()