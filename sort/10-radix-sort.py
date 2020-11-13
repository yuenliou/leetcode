#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

"""
https://blog.csdn.net/qq_25026989/article/details/89367954
基数排序、桶排序和计数排序的区别：

1.桶排序(Bucket Sort)
基本思路是：
将待排序元素划分到不同的痛。先扫描一遍序列求出最大值 maxV 和最小值 minV ，
设桶的个数为 k ，则把区间 [minV, maxV] 均匀划分成 k 个区间，每个区间就是一个桶。将序列中的元素分配到各自的桶。
对每个桶内的元素进行排序。可以选择任意一种排序算法。
 将各个桶中的元素合并成一个大的有序序列。
假设数据是均匀分布的，则每个桶的元素平均个数为 n/k 。假设选择用快速排序对每个桶内的元素进行排序，
那么每次排序的时间复杂度为 O(n/klog(n/k)) 。
总的时间复杂度为 O(n)+O(m)O(n/klog(n/k)) = O(n+nlog(n/k)) = O(n+nlogn-nlogk 。
当 k 接近于 n 时，桶排序的时间复杂度就可以金斯认为是 O(n) 的。即桶越多，时间效率就越高，而桶越多，空间就越大。

2.计数排序(Counting Sort)
是一种O(n)的排序算法，其思路是开一个长度为 maxValue-minValue+1 的数组，然后
分配。扫描一遍原始数组，以当前值- minValue 作为下标，将该下标的计数器增1。
收集。扫描一遍计数器数组，按顺序把值收集起来。
举个例子， nums=[2, 1, 3, 1, 5] , 首先扫描一遍获取最小值和最大值，
 maxValue=5 , minValue=1 ，于是开一个长度为5的计数器数组 counter ，
1. 分配。统计每个元素出现的频率，得到 counter=[2, 1, 1, 0, 1] ，例如 counter[0] 表示值 0+minValue=1 出现了2次。
2. 收集。 counter[0]=2 表示 1 出现了两次，那就向原始数组写入两个1，
3. counter[1]=1 表示 2 出现了1次，那就向原始数组写入一个2，依次类推，最终原始数组变为 [1,1,2,3,5] ，排序好了。
  计数排序本质上是一种特殊的桶排序，当桶的个数最大的时候，就是计数排序。

3.基数排序
是一种非比较排序算法，时间复杂度是 O(n) 。它的主要思路是，
1. 将所有待排序整数（注意，必须是非负整数）统一为位数相同的整数，位数较少的前面补零。一般用10进制，
2. 也可以用16进制甚至2进制。所以前提是能够找到最大值，得到最长的位数，设 k 进制下最长为位数为 d 。
3. 从最低位开始，依次进行一次稳定排序。这样从最低位一直到最高位排序完成以后，整个序列就变成了一个有序序列。
举个例子，有一个整数序列，0, 123, 45, 386, 106，下面是排序过程：
第一次排序，个位，000 123 045 386 106，无任何变化
第二次排序，十位，000 106 123 045 386
第三次排序，百位，000 045 106 123 386
最终结果，0, 45, 106, 123, 386, 排序完成。
为什么同一数位的排序子程序要用稳定排序？因为稳定排序能将上一次排序的成果保留下来。
例如十位数的排序过程能保留个位数的排序成果，百位数的排序过程能保留十位数的排序成果。
能不能用2进制？能，可以把待排序序列中的每个整数都看成是01组成的二进制数值。
那这样的话，岂不是任意一个非负整数序列都可以用基数排序算法？
理论上是的，假设待排序序列中最大整数为2 4 . 1，则最大位数 d=64 ，时间复杂度为 O(64n) 。
可见任意一个非负整数序列都可以在线性时间内完成排序。
既然任意一个非负整数序列都可以在线性时间内完成排序，那么基于比较排序的算法有什么意义呢？
基于比较的排序算法，时间复杂度是 O(nlogn) ，看起来比 O(64n) 慢，仔细一想，其实不是， O(nlogn) 只有当序列非常长，
达到2^64 个元素的时候，才会与 O(64n) 相等，因此，64这个常数系数太大了，
大部分时候， n 远远小于2^64，基于比较的排序算法还是比 O(64n) 快的。
当使用2进制时， k=2 最小，位数 d 最大，时间复杂度 O(nd) 会变大，空间复杂度 O(n+k) 会变小。
当用最大值作为基数时， k=maxV 最大， d=1 最小，此时时间复杂度 O(nd) 变小，
但是空间复杂度 O(n+k) 会急剧增大，此时基数排序退化成了计数排序
"""

def radixSort(arr):
    """
    工作原理：基数排序(Radix Sort)是桶排序的扩展
    编码要素：计数排序要求输入的数据必须是有确定范围的整数

    基数排序分LSD（Least significant digital）和MSD（Most significant digital）
    LSD的排序方式由键值的最右边开始，而MSD则相反，由键值的最左边开始。
    """
    #加减乘除模：add, subtract, multiply and divide，mod
    mod = 10
    div = 1
    maxVal = max(arr)
    while maxVal: # 最大数的宽度
        # 初始化10个桶
        buckets = [[] for _ in range(10)]
        # 初始化元素(lsd)
        for val in arr: #有记忆的数组，会记住上次循环的顺序
            bucket = val % mod // div
            buckets[bucket].append(val)
        # 按桶的顺序重新加入
        arr.clear()
        # buckets.reverse() # 逆序
        # print(buckets)
        for bucket in buckets:
            while len(bucket):
                arr.append(bucket.pop(0))

        mod *= 10
        div *= 10
        maxVal //= 10
    return arr

def radixSort_v2(arr):

    def countSort(arr, div):
        # 计数排序
        buckets = [0 for _ in range(10)]
        #将数据出现的次数存储在buckets[]中
        for val in arr:
            buckets[val//div%10] += 1
        #更改buckets[i] 目的是让更改后的buckets[i]的值，是该数据在output[]中的位置
        #buckets[i] > 1,则在output中预留空位
        for i in range(1, 10):
            buckets[i] += buckets[i-1]

        # buckets[i]是从远到近递减，所以需要翻转下
        arr.reverse()
        #存储"被排序数据"的临时数组
        output = [0] * len(arr)
        for i, val in enumerate(arr):
            output[buckets[val//div%10]-1] = val
            buckets[val//div%10] -= 1
        # print(output)
        return output

    div = 1
    maxVal = max(arr)
    while maxVal:
        arr = countSort(arr, div)
        div *= 10
        maxVal //= 10
    return arr

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = radixSort_v2(arr)
    print(ret)

if __name__ == '__main__':
    main()
