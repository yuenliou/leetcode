#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    """暴力枚举：https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/bao-li-jie-fa-qian-zhui-he-qian-zhui-he-you-hua-ja/"""
    length = len(nums)
    if length <= 0: return -1

    count = 0

    #暴力1：枚举左右边界（超时）n*n*n
    # for i in range(0, length):#left
    #     for j in range(i, length):#right
    #         sum = 0
    #         for n in range(i, j+1):#[left,right]
    #             sum += nums[n]
    #         #求和之后对比
    #         if sum == k:
    #             count += 1

    #暴力优化2：先固定左边界，然后枚举右边界 n*n
    for i in range(0, length):
        sum = 0
        for j in range(i, length):#gap++
            # print(i, j)
            sum += nums[j]
            if sum == k:
                count += 1

    return count

def subarraySum0(nums: List[int], k: int) -> int:
    """前缀和优化"""
    length = len(nums)
    if length <= 0: return -1

    sum = [0] * len(nums)

    #前缀和
    sum[0] = nums[0]
    for i in range(1, length):
        sum[i] = sum[i-1] + nums[i]

    #sum[i] - sum[j] == k
    count = 0
    for i in range(0, length):
        for j in range(-1, i):
            if j == -1:#处理单元素情况
                if sum[i] == k:
                    count += 1
            else:
                if sum[i] - sum[j] == k:
                    count += 1
    return count

def subarraySum1(nums: List[int], k: int) -> int:
    """前缀和优化"""
    length = len(nums)
    if length <= 0: return -1

    #前缀和n+1项
    sum = [0] * (len(nums) + 1)
    sum[0] = 0
    for i in range(0, length):
        sum[i+1] = sum[i] + nums[i]

    count = 0
    for i in range(0, length):
        for j in range(i, length):
            # 区间和[left..right]，注意下标偏移
            if sum[j + 1] - sum[i] == k:
                count += 1
    return count

def subarraySum2(nums: List[int], k: int) -> int:
    """前缀和+map"""
    length = len(nums)
    if length <= 0: return -1

    sum = [0] * len(nums)
    #前缀和
    sum[0] = nums[0]
    for i in range(1, length):
        sum[i] = sum[i-1] + nums[i]

    # map<前i个元素的前缀和，出现的次数> 默认值：特殊情况，和等于某个元素
    dict = {0:1}

    #dict[sum[i] - k] = sum[j]
    count = 0
    for s in sum:
        if s - k in dict:
            count += dict[s - k]
        dict[s] = dict.get(s, 0) + 1
    return count

def subarraySum3(nums: List[int], k: int) -> int:
    """前缀和+map"""
    length = len(nums)
    if length <= 0: return -1

    # map<前i个元素的前缀和，出现的次数> 默认值：特殊情况，和等于某个元素
    dict = {0:1}

    #前缀和
    pre = 0
    count = 0
    for i in range(0, length):
        pre += nums[i]
        if pre - k in dict:
            count += dict[pre - k]
        dict[pre] = dict.get(pre, 0) + 1
    return count


def main():
    param = [1]
    param = [1, 1, 1]
    param = [1, 2, 3, 4, 5]
    ret = subarraySum1(param, 3)
    print(ret)

'''560. 和为K的子数组

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
