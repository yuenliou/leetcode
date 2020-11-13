#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def heapSort(arr):
    """
    工作原理：最大堆，最小堆
    编码要素：下沉down，上浮up；demotion，promotion
    """
    def down_recur(arr, i, n):
        """堆化(递归)：堆的向下调整算法"""
        current = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        if l < n and arr[l] > arr[current]:
            current = l
        if r < n and arr[r] > arr[current]:
            current = r

        if current != i:
            arr[i], arr[current] = arr[current], arr[i]  # 交换
            down_recur(arr, current, n) # 下沉

    # 构建最大堆
    n = len(arr)
    # heapify
    for i in reversed(range(n // 2)):
        down_recur(arr, i, n)  # 建立堆

    # sort
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        down_recur(arr, 0, i)  # 调整0

    return arr

def heapSort_v2(arr):
    """
    工作原理：最大堆，最小堆
    编码要素：下沉down，上浮up；demotion，promotion
    """
    def down_iter(arr, i, n, comp):
        """堆化(迭代)：堆的向下调整算法"""
        current = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        while True:
            if l < n and comp(arr[l], arr[current]):
                current = l
            if r < n and comp(arr[r], arr[current]):
                current = r
            if current == i: break
            # 交换
            arr[i], arr[current] = arr[current], arr[i]

            # 下一轮左右节点
            i = current
            l = 2 * i + 1
            r = 2 * i + 2

    def heapifyAndSort(arr, comp):
        """构建堆"""
        n = len(arr)
        #heapify
        for i in reversed(range(n // 2)):
            down_iter(arr, i, n, comp) #建立堆

        # sort
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # 交换
            down_iter(arr, 0, i, comp)  # 调整0

    # build a heap with comp
    # 升序
    # heapifyAndSort(arr, lambda x, y: x > y)
    # 降序
    heapifyAndSort(arr, lambda x, y: x < y)

    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    # arr = [20,30,90,40,70,110,60,10,100,50,80]
    #maxheap: [110, 100, 90, 40, 80, 20, 60, 10, 30, 50, 70]
    #minheap: [10, 20, 60, 30, 50, 110, 90, 40, 100, 70, 80]
    ret = heapSort(arr)
    print(ret)

if __name__ == '__main__':
    main()
