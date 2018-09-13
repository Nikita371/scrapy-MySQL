# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb
from hhparser import settings


class HhparserPipeline(object):
        
    def __init__(self):
        self.conn =  MySQLdb.connect
        conn = MySQLdb.connector.Connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor() 
        cur = mysql.connection.cursor()


    def process_item(self, item, spider):    
            self.cursor.execute("""insert into hhvacancy (id,Salary, Employer, Vacancy) value(%s,%s, %s, %s)""", 
                        (1,'10000',
                 'Gazprom',
                 'Manager',
                 ))          
            self.conn.commit()    