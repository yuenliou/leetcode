#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import re,time,datetime,os,os.path,sys,shutil,pickle,math,random,itertools,functools,sqlite3
import subprocess,signal,threading,multiprocessing
import socket,requests,urllib,django
from queue import Queue, SimpleQueue, LifoQueue, PriorityQueue
#实际上，Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块
import heapq
#提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择
#https://docs.python.org/zh-cn/3.7/library/collections.html
from collections import ChainMap, namedtuple, deque, Counter, OrderedDict, defaultdict, UserDict, UserList, UserString

def timestamp():
    print(int(time.time()))
    print(int(time.time() * 1000))
    print(int(time.time() * 1000 ** 2))
    print(time.time_ns())

def comprehension():
    """
    列表推导式 list comprehension
    生成器推导式 generator comprehension
    数组推导式 array comprehension ; Array comprehensions
    字典推导式 Dictionary comprehensions
    链表推导式 List Comprehensions
    推导式流量计 inferential flowmeter
    合推导式 Set Comprehensions
    嵌套列表推导式 Nested List Comprehensions
    推导式演进特征投影法 heuristic evolvimg latent projections
    """

    '''
    语法：
        变量名 = [表达式 for 变量 in 列表 for 变量 in xxx]
        变量名 = [表达式 for 变量 in 列表 if 条件]
    语义：
        遍历出列表中的内容给变量，表达式根据变量值进行逻辑运算。或者遍历列表中的内容给变量，然后进行判断，符合的值在给表达式。
    '''
    #list
    l = [x * x for x in range(1, 11)]
    print(l)
    l2 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(l2) #if
    l3 = [m + n for m in 'ABC' for n in 'XYZ']
    print(l3) #两层

    # 此处定义了一个装了 3 个匿名函数函数的列表，尚未调用匿名函数，
    # 调用时全局变量 i 变为 2 相当于 a = [lambda x:x*2, lambda x:x*2, lambda x:x*2]
    a = [lambda x: x * i for i in range(3)]
    print(a[0](2)) # 4
    print(a[1](2)) # 4
    print(a[2](2)) # 4

    #tuple
    #使用元组推导式生成的结果不是一个元组或者列表，而是一个生成器对象，这一点和列表生成器是不同的
    t = (random.randint(i, 10) for i in range(10))
    print(t) #<generator object <genexpr> at 0x102bb8570>
    print(tuple(t)) #(0, 9, 3, 10, 9, 8, 6, 8, 10, 9)
    print(list(t)) #[] 只能生成一次
    '''
    什么是生成器. 生成器实质就是迭代器.
    在python中有三种方式来获取生成器:
    1. 通过生成器函数yield
    2. 通过各种推导式来实现生成器 (生成器表达式)
    3. 通过数据的转换也可以获取生成器
    '''

    #dict
    inorder = [9, 3, 15, 20, 7]
    index = {element: i for i, element in enumerate(inorder)}
    print(index)

    #set
    set1 = {x for x in range(10) if x % 2 == 0}
    print(set1)
    '''总结: 推导式有, 列表推导式, 字典推导式, 集合推导式, 没有元组推导式'''


def foreachList():

    list_product = ["thinkpad", "macbook", "iphone8", "robbit"]

    print('--遍历数组--')
    for v in list_product:
        print(v)

    print('--遍历数组+索引1--')
    for key in range(len(list_product)):
        print(key + 1, list_product[key])

    print('--遍历数组+索引2--')
    for key, v in enumerate(list_product, 1):
        print(key, v)

    # aa = set(list_product)

    # 集合交叉并补-数组/字典需要转换成集合
    a = set([1, 2, 3, 4, 5, 100, 1000])
    b = set([1, 2, 3, 4, 5, 128.1024])
    # 交集
    print(a & b)  # {1, 2, 3, 4, 5}
    print(a.intersection(b))  # {1, 2, 3, 4, 5}
    # 差集
    print(a - b)  # {1000, 100}
    print(a.difference(b))  # {1000, 100}

    # 并集
    print(a | b)  # {128.1024, 1, 2, 3, 4, 5, 100, 1000}
    print(a.union(b))  # {128.1024, 1, 2, 3, 4, 5, 100, 1000}

    # 对称差集--返回两个集合中不重复的元素
    print(a ^ b)  # {128.1024, 100, 1000}
    print(a.symmetric_difference(b))  # {128.1024, 100, 1000}

    # for _ in range(16):
    #     print('noodles')

    x = 'ABC'
    y = x.encode('ascii') # b'ABC'
    print(y)


def main():
    # foreachList()
    comprehension()

if __name__ == '__main__':
    main()
