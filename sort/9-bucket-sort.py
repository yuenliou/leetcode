#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import math

def bucketSort(arr):
    """
    工作原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
    编码要素：桶排序是计数排序的升级版。用了函数的映射关系，高效与否的关键就在于这个映射函数的确定
    """

    minVal = min(arr)
    maxVal = max(arr)

    # 默认桶数量
    bucketSize = 5
    # 桶初始化
    bucketCount = math.floor((maxVal - minVal) / bucketSize)
    # buckets = [[]] * (bucketCount + 1) #这种写法内层是同一个数组对象，浅copy
    # buckets = [list() for _ in range(bucketCount + 1)] #推导式这种写法则会生成独立的list对象
    buckets = []
    for i in range(bucketCount + 1):
        buckets.append([])
    # 利用映射函数将数据分配到各个桶中
    for val in arr:
        buckets[math.floor((val - minVal) / bucketSize)].append(val)

    arr.clear()

    #根据bucket填充目标数组
    for j, bucket in enumerate(buckets):
        # 对每个桶进行排序，这里使用了插入排序
        bucket = sorted(bucket)
        while len(bucket):
            arr.append(bucket.pop(0))

    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = bucketSort(arr)
    print(ret)

if __name__ == '__main__':
    main()
