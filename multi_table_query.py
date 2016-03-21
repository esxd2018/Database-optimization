# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/18
Last Modify: 2016/3/21
version: 0.0.1
'''

import os

def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files
for file in index("./data/"):
    print file
