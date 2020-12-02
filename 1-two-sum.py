#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """枚举:n*n"""
    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i ,j]
    return []

def twoSum1(nums: List[int], target: int) -> List[int]:
    """map优化:n时间+n空间"""
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

def main():
    nums = [2, 7, 11, 15]
    target = 9
    ret = twoSum(nums, target)
    print(ret)

'''1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
