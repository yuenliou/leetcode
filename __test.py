#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import re,time,datetime,os,os.path,sys,shutil,pickle,math,random,itertools,functools,sqlite3
import subprocess,signal,threading,multiprocessing
import socket,requests,urllib,django


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
    foreachList()

if __name__ == '__main__':
    main()
