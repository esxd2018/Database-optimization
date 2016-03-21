# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   初始化数据库demo

My Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/18
Last Modify: 2016/3/21
version: 0.0.1
'''

import os
import random
from db_server import DatabaseServer

INSERT_STUDENT_SQL = "INSERT INTO student(school_id, name, sex, age, class_name) VALUES({0}, \'{1}\', {2}, {3}, {4});"
INSERT_CLASS_SQL = "INSERT INTO class(class_name, master_id, is_key) VALUES({0}, {1}, {2});"
INSERT_COURSE_SQL = \
    "INSERT INTO course(course_name, grade, president_id, is_neces, credit) VALUES({0}, {1}, {2}, 1, 4);"
school_id = 100001

def init_student(students, class_name):
    global school_id
    db = DatabaseServer("school")
    for student in students:
        name = student[:-2]
        sql = INSERT_STUDENT_SQL.format(school_id, "{0}".format(name), random_sex(), random_age(), class_name)
        print(sql)
        db.update(sql)
        school_id += 1
    db.close()
    pass

def init_class(class_name):
    db = DatabaseServer("school")
    sql = INSERT_CLASS_SQL.format(class_name, 1, 0)
    db.update(sql)
    db.close()
    pass

def init_course():
    # INSERT INTO course(course_name, grade, president_id, is_neces, credit) VALUES('Chinese', 1, 100001, 1, 4);
    # sql = INSERT_STUDENT_SQL.format(school_id, "{0}".format(name), random_sex(), random_age(), class_name)
    pass

# TODO-[INSERT INTO score(course_id, school_id, score) VALUES(1, 100005, 88);]
def init_score():
    db = DatabaseServer("school")
    sids = db.select("SELECT school_id FROM student;")  # 学号
    for sid in sids:
        # print(sid[0])
        res = db.select(
            "SELECT c.id FROM course c WHERE c.class_name="
            "(SELECT s.class_name FROM student s WHERE school_id={0});"
                .format(sid[0]))
        for r in res:
            print("{0}-{1}".format(sid[0], r[0]))
            db.update("INSERT INTO score(course_id, school_id, score) VALUES({0}, {1}, {2});".format(r[0], sid[0], random_score()))
        pass
    db.close()
    pass

def random_sex():
    return int(random.uniform(0, 2))

def random_age():
    return int(random.uniform(14, 20))

def random_score():
    return int(random.uniform(40, 100))

def file_index(directory):
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file_name in os.listdir(directory):
            fullname = os.path.join(directory, file_name)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files

def read_lines(file_dir):
    student_file = open(file_dir, "rb")
    return student_file.readlines()

for filename in file_index("./data/"):
    # print filename
    file_name = filename.split("/")[2]
    # init_student(read_lines(filename), file_name)
    # init_class(file_name)
    init_score()
    break
