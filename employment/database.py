# -*- coding: utf-8 -*-

import pymysql

# def insert(item):
#     db = pymysql.connect('localhost', 'smu', '20131498675MUsheng', 'musheng')
#     cursor = db.cursor()
#
#     sql = """create table `employment` (
#       `id` int(11) NOT NULL AUTO_INCREMENT,
#       `title` varchar(255) COLLATE utf8_bin NOT NULL,
#       `feedback` varchar(20) COLLATE utf8_bin,
#       `company` varchar(255) COLLATE utf8_bin,
#       `salary` varchar(20) COLLATE utf8_bin,
#       `location` varchar(255) COLLATE utf8_bin,
#       `date` varchar(20) COLLATE utf8_bin,
#        PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""
#     # 使用 fetchone() 方法获取单条数据.
#
#     insert_sql = "INSERT INTO `employment` (`title`, `feedback`, `company`, `salary`, `location`, `date`) VALUES (%s, %s, %s, %s, %s, %s)"
#
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         raise
#
#     # 关闭数据库连接
#     db.close()

def initDB():
    db = pymysql.connect('localhost', 'smu', '20131498675MUsheng', 'musheng', charset='utf8mb4')
    return db

def insert(self, item):
    insert_sql = "INSERT INTO `employment` (`title`, `feedback`, `company`, `salary`, `location`, `date`) VALUES (%s, %s, %s, %s, %s, %s)"
    db = self.db
    cursor = db.cursor()
    try:
        title = item['title']
        feedback = item['feedback']
        company = item['company']
        salary = item['salary']
        location = item['location']
        date = item['date']
        cursor.execute(insert_sql, (title, feedback, company, salary, location, date))
        db.commit()
    except Exception as e:
        db.rollback()
        raise
