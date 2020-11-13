#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def insertionSort(arr):
    """
    工作原理：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    编码要素：外层控制循环次数，内层从后向前扫描(最优，交换次数最少)
    """
    length = len(arr)
    for i in range(1, length):
        preIndex = i - 1
        current = arr[i]
        # 已排序序列中从后向前扫描
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr

def insertionSort2(arr):
    length = len(arr)
    for i in range(1, length):
        # 从后向前扫描，不能直接交换，处理比较复杂
        # for j in range(i - 1, -1, -1):
        # 从前向后扫描
        for j in range(0, i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = insertionSort(arr)
    print(ret)

if __name__ == '__main__':
    main()
