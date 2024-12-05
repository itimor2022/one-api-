# -*- coding: utf-8 -*-
# author: itimor
# pip3 install PyMySQL

# import  MySQLdb
import pymysql as MySQLdb


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

if __name__ == '__main__':
    xxljob_info = {
        "host": "172.31.250.114",
        "port": 3306,
        "user": "canal",
        "passwd": "canal",
        "db": "canal_manager_test",
    }
    jobapi = MYSQL(xxljob_info)
    for i in range(1000000):
        print(i)
        sql = f"INSERT INTO `canal_manager_test`.`es_suggest_key` (`keyword`,`keyword_type`,`weight`) VALUES ('aaa',{i},{i});"
        jobapi.insert(sql)
    jobapi.close()