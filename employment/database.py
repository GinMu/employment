# -*- coding: utf-8 -*-

import pymysql

# db = pymysql.connect('localhost', 'smu', '20131498675MUsheng', 'musheng')
# cursor = db.cursor()
#
# sql = """create table `employment` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `title` varchar(255) COLLATE utf8_bin NOT NULL,
#   `feedback` varchar(20) COLLATE utf8_bin,
#   `company` varchar(255) COLLATE utf8_bin,
#   `min_salary` int(10) COLLATE utf8_bin,
#   `max_salary` int(10) COLLATE utf8_bin,
#   `location` varchar(255) COLLATE utf8_bin,
#   `date` varchar(20) COLLATE utf8_bin,
#    PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     db.rollback()
#     raise
#
# # 关闭数据库连接
# db.close()

def initDB():
    db = pymysql.connect('localhost', 'smu', '20131498675MUsheng', 'musheng', charset='utf8mb4')
    return db

def initCursor(self):
    cursor = self.db.cursor()
    return cursor

def clearData(self):
    clear_sql = "truncate employment"
    try:
        self.cursor.execute(clear_sql)
        pass
    except Exception as e:
        raise

def insertData(self, item):
    insert_sql = "INSERT INTO `employment` (`title`, `feedback`, `company`, `min_salary`, `max_salary`, `location`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    db = self.db
    cursor = self.cursor
    try:
        title = item['title']
        feedback = item['feedback']
        company = item['company']
        min_salary = item['min_salary']
        max_salary = item['max_salary']
        location = item['location']
        date = item['date']
        cursor.execute(insert_sql, (title, feedback, company, min_salary, max_salary, location, date))
        db.commit()
        pass
    except Exception as e:
        db.rollback()
        raise
