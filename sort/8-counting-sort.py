#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def countingSort(arr):
    """
    工作原理：其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中
    编码要素：计数排序要求输入的数据必须是有确定范围的整数
    """

    #序列比较集中，如果过大：基于0的偏移量
    #将数组长度定为max-min+1，即不仅要找出最大值，还要找出最小值，根据两者的差来确定计数数组的长度。
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

def countingSort_v2(arr):
    """
    工作原理：其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中
    编码要素：计数排序要求输入的数据必须是有确定范围的整数
    一文弄懂计数排序算法！https://www.cnblogs.com/xiaochuan94/p/11198610.html
    """

    #value映射到index
    bucket = [0] * (max(arr) + 1)
    for i, val in enumerate(arr):
        bucket[val] += 1

    # print(bucket)

    #调整bucket[i]的值，是该数据在output[]中的位置
    for i in range(1, len(bucket)):
        bucket[i] += bucket[i - 1]

    # print(bucket)
    """
    第五步：创建结果数组result，长度和原始数组一样。

    第六步：遍历原始数组中的元素，当前元素A[j]减去最小值min，作为索引，在计数数组中找到对应的元素值count[A[j]-min]，再将count[A[j]-min]的值减去1，就是A[j]在结果数组result中的位置，做完上述这些操作，count[A[j]-min]自减1。
    
    是不是对第四步和第六步有疑问？为什么要这样操作？
    
    第四步操作，是让计数数组count存储的元素值，等于原始数组中相应整数的最终排序位置，即计算原始数组中的每个数字在结果数组中处于的位置。
    
    比如索引值为9的count[9]，它的元素值为10，而索引9对应的原始数组A中的元素为9+101=110（要补上最小值min，才能还原），即110在排序后的位置是第10位，即result[9] = 110，排完后count[9]的值需要减1，count[9]变为9。
    
    再比如索引值为6的count[6]，他的元素值为7，而索引6对应的原始数组A中的元素为6+101=107，即107在排序后的位置是第7位，即result[6] = 107，排完后count[6]的值需要减1，count[6]变为6。
    
    如果索引值继续为6，在经过上一次的排序后，count[6]的值变成了6，即107在排序后的位置是第6位，即result[5] = 107，排完后count[6]的值需要减1，count[6]变为5。
    
    至于第六步操作，就是为了找到A中的当前元素在结果数组result中排第几位，也就达到了排序的目的。
    """

    #a[13] = 50：output[bucket[a[13] - 1]] = output[49] = 14
    output = [0] * len(arr)
    for i in range(len(arr)):
        output[bucket[arr[i] - 1]] = arr[i]
        bucket[arr[i] - 1] -= 1
    return output

def main():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
    ret = countingSort_v2(arr)
    print(ret)

if __name__ == '__main__':
    main()
