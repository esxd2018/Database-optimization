# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 数据库的链接核心程序

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/18
version: 0.0.1
'''

import MySQLdb
import db_config as conf

class DatabaseServer(object):
    # ----------------------------------------- #
    # 默认的初始化方法                             #
    # ----------------------------------------- #
    def __init__(self, db_name=None):
        self.__host = conf.DB_HOST
        self.__user = conf.DB_USER
        self.__passwd = conf.DB_PASSWD
        if db_name is None:
            self.__db_name = conf.DB_NAME
        else:
            self.__db_name = db_name
        self.__port = conf.DB_PORT
        self.__charset = conf.DB_CHARSET
        self.__connection = None
        self.__cursor = None

        self.__init_database()

    # ----------------------------------------- #
    # 初始化数据库的相关信息                        #
    # 可见性：内部可见                             #
    # ----------------------------------------- #
    def __init_database(self):
        self.__connect_database()
        if self.__connection:
            self.__cursor = self.__connection.cursor()
            self.__check_select()

    # ----------------------------------------- #
    # 检查并选择一个数据库进行操作                   #
    # 可见性：内部可见                             #
    # ----------------------------------------- #
    def __check_select(self):
        try:
            # self.__cursor.execute('CREATE DATABASE if not exists ' + self.__db_name)
            self.__connection.select_db(self.__db_name)
            self.__connection.commit()
        except Exception as e:
            print("Check your database has a exception: {0}".format(e))

    # ----------------------------------------- #
    # 连接数据库                                  #
    # 可见性：内部可见                             #
    # ----------------------------------------- #
    def __connect_database(self):
        try:
            self.__connection = MySQLdb.connect(
                host=self.__host,
                user=self.__user,
                passwd=self.__passwd,
                port=self.__port,
                charset=self.__charset
            )
        except Exception as e:
            print("Connect database failed, {0}".format(e))
            self.__connection = None

    # ----------------------------------------- #
    # 获取查询结果集(全部)                         #
    # 可见性：公开可见                             #
    # ----------------------------------------- #
    def select(self, sql):
        """
        获取查询结果集(全部)
        """
        result_set = None
        if self.__connection:
            try:
                self.__cursor.execute(sql)
                result_set = self.__cursor.fetchall()
            except Exception as e:
                result_set = None
                print("Query database exception, {0}".format(e))
        return result_set

    # ----------------------------------------- #
    # 更新数据库                                  #
    # 可见性：公开可见                             #
    # ----------------------------------------- #
    def update(self, sql):
        """
        全部的更新操作
        """
        flag = False
        if self.__connection:
            try:
                self.__cursor.execute(sql)
                self.__connection.commit()
                flag = True
            except Exception as e:
                flag = False
                print("Update database exception, {0}".format(e))
        return flag

    # ----------------------------------------- #
    # 获得数据库名称信息                           #
    # 可见性：公开可见                             #
    # ----------------------------------------- #
    def get_db_name(self):
        """
        获得数据库名称信息
        """
        return self.__db_name

    # ----------------------------------------- #
    # 关闭数据库连接                               #
    # 可见性：公开可见                             #
    # ----------------------------------------- #
    def close(self):
        """
        关闭数据库连接
        """
        if self.__connection:
            try:
                if isinstance(self.__cursor, MySQLdb.cursors.Cursor):
                    self.__cursor.close()
                if isinstance(self.__connection, MySQLdb.connections.Connection):
                    self.__connection.close()
            except Exception as e:
                print("Close database exception, {0}, {1}, {2}".format(e, type(self.__cursor), type(self.__connection)))
        else:
            print("MySQL connection is None.")
