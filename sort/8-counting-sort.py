#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def countingSort(arr):
    """
    工作原理：其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中
    编码要素：计数排序要求输入的数据必须是有确定范围的整数
    """

    #序列比较集中，如果过大：基于0的偏移量
    # bucket = [0] * (max(arr) + 1)
    bucket = [0 for _ in range(max(arr) + 1)]
    for i, val in enumerate(arr):
        bucket[val] += 1

    sortedIndex = 0
    #根据bucket反向填充目标数组
    for j, val in enumerate(bucket):
        while val > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            val -= 1
    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = countingSort(arr)
    print(ret)

if __name__ == '__main__':
    main()
