#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import math

def shellSort(arr):
    length = len(arr)
    # gap为步长，每次减为原来的一半。
    gap =  math.floor(length / 2) # 步长
    while gap > 0:
        for i in range(gap): # 共gap个组
            for j in range(i+gap, length, gap): # 对每一组都执行直接插入排序
                preIndex = j - gap
                current = arr[j]
                while preIndex >= 0 and arr[preIndex] > current:
                    arr[preIndex + gap] = arr[preIndex]
                    preIndex -= gap
                arr[preIndex + gap] = current
        gap = math.floor(gap / 2)
    return arr

def shellSort2(arr):
    """工作原理：缩小增量排序，与直接插入排序的不同之处在于，它会优先比较距离较远的元素"""
    length = len(arr)
    gap = 1
    # 获取最大步长，可取值有4、13、40、121、364、1093....
    while gap < length // 3: # 动态定义间隔序列
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, length):
            preIndex = i - gap
            current = arr[i] # 待排的元素
            while preIndex >= 0 and arr[preIndex] > current:
                arr[preIndex + gap] = arr[preIndex] # 值大的后移, 腾出位置,等待填充
                preIndex -= gap
            arr[preIndex + gap] = current # 找到合适的位置，填充进去
        # gap //= 3 # 4、13、40...gap取这些值，等同于下面写法
        gap = (gap - 1) // 3 # 改变步长
    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    # arr = [84, 83, 88, 87, 61, 50, 70, 60, 80, 90]
    # arr = [5, 2, 4, 3, 1]
    ret = shellSort(arr)
    print(ret)

def testGap(length, gap):
    """v1两层for range(gap) <==> v2一层for range(gap, length)"""
    for i in range(gap):
        for j in range(i + gap, length, gap):
            print(j)
            # print(j, j-gap, sep='-')
            # print(j, i, sep='-') #0[2468],1[357]
    print('--------')
    for i in range(gap, length):
        print(i)
        # print(i, i - gap, sep='-')
    print('\n')

if __name__ == '__main__':
    main()
    # testGap(8, 2) #246357,234567
    # testGap(8, 4) #4567,4567
    testGap(9, 2) #2468357,2345678
    # testGap(10, 2) #24683579,23456789
    # testGap(10, 3) #3694758,3456789
    # testGap(10, 4) #485967,456789
    # testGap(10, 5) #56789,56789
