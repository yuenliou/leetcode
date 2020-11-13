#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def selectionSort(arr):
    """
    工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    编码要素：外层控制循环次数，内层选择最小元素
    """
    length = len(arr)
    for i in range(length):
        minIndex = i
        for j in range(i+1, length):
            if arr[j] < arr[minIndex]:
                # 未排序序列中最小元素
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = selectionSort(arr)
    print(ret)

if __name__ == '__main__':
    main()
