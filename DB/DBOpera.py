import pymysql
from . import DBUtils

class DBOpera():

    def __init__(self,user,password,db_name):
        self.user = user
        self.password = password
        self.db = pymysql.connect("localhost",user,password,db_name)

    def insert(self,table_name,data_list):
        status = False
        err = None
        cursor = self.db.cursor()
        parse = "insert into %s values (%s)" % (table_name,DBUtils.listToString(data_list))
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit()
            status = True
            err = None
        except Exception as e:
            status = False
            err  = e
        return (status,err)
    
    def delete(self,table_name,attr_list,data_list):
        status = False
        err = None
        cursor = self.db.cursor()
        parse = "delete from %s where %s" % (table_name,DBUtils.twoListToCond(attr_list,data_list))
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit()
            status = True
            err = None
        except Exception as e:
            status = False
            err = e
        return (status,err)

    def query(self,table_name,attr_list,data_list): 
        status = False
        err = None
        res = None
        cursor = self.db.cursor()
        parse = "SELECT * FROM %s" % (table_name,)
        if(len(attr_list) != 0):
            parse = "SELECT * FROM %s where %s" % (table_name,DBUtils.twoListToCond(attr_list,data_list))
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit() 
            status = True
            err = None
            res = cursor.fetchall() 
        except Exception as e:
            status = False
            err = e
            res = None
        return (status,err,res)

    def __del__(self):
        self.db.close()
