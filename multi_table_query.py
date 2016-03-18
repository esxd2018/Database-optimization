# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/18
Last Modify: 2016/3/18
version: 0.0.1
'''

import string

if __name__ == '__main__':
    a = "a b c      d e f"
    b = string.split(a)
    c = string.join(b, '+')
    print(b)
    print(c)
    pass
