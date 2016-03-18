# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 测试SQL注入

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/9
Last Modify: 2016/3/9
version: 0.0.1
'''

import db_server as db1

CREATE_TABLE_SQL = 'CREATE TABLE student(id INT, name TEXT, sex INT, age INT);'
INSERT_SQL = 'INSERT student(id, name, sex, age) VALUES(1, \'Alice\', 1, 18);'

ORIGINAL_SQL = "SELECT name, age, sex FROM student WHERE "  # 原始SQL语句
INJECT_SQL = 'name=\'Bob\' or 1=1;'  # 待注入的SQL语句

def inject(value):
    return ORIGINAL_SQL + value

def execute():
    db_helper = db1.DatabaseServer('school')
    sql = inject(INJECT_SQL)
    result = db_helper.select(sql)
    print(result)

if __name__ == '__main__':
    execute()
    pass

