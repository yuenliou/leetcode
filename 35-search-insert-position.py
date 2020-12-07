#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    # 二分
    n = len(nums)
    i, j = 0, n - 1
    while i <= j:
        k = ((j - i) >> 1) + i
        if nums[k] == target:
            return k
        if nums[k] > target:
            j = k - 1
        if nums[k] < target:
            i = k + 1
    return i

def main():
    param = [1,3,5,6]
    ret = searchInsert(param, 7)
    print(ret)

'''35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
