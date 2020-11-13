#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

"""
十大经典排序算法（动图演示）
https://www.cnblogs.com/markstray/p/10013768.html
数据结构与算法系列 目录
https://www.cnblogs.com/skywang12345/p/3603935.html
"""
def bubbleSort(arr):
    """
    工作原理：重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来
    编码要素：外层控制循环次数，内层比较相邻元素
    """
    length = len(arr)
    for i in range(length):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                # 相邻元素交换
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = bubbleSort(arr)
    print(ret)

if __name__ == '__main__':
    main()
