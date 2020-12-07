#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def search(nums: List[int], target: int) -> int:
    """带等号写法：i/left，j/right，k/mid"""
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
    return -1

def search1(nums: List[int], target: int) -> int:
    """不带等号写法：左边界
    【搜索区间定乾坤】
    while(left <= right) 的终止条件是 left == right + 1；区间是空，循环体中查找元素
    while(left < right) 的终止条件是 left == right；区间非空，循环体中排除目标元素一定不存在的区间
    https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/

    思路 1：在循环体中查找元素；
    思路 2：在循环体中排除目标元素一定不存在的区间。

    边界设置的两种写法：
    right = mid 和 left = mid + 1 和 int mid = left + (right - left) / 2; 一定是配对出现的；
    right = mid - 1 和 left = mid 和 int mid = left + (right - left + 1) / 2; 一定是配对出现的。

    作者：liweiwei1419
    链接：https://leetcode-cn.com/leetbook/read/learning-algorithms-with-leetcode/xs41qg/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    n = len(nums)
    i, j = 0, n - 1
    while i < j:
        k = ((j - i) >> 1) + i
        # print(i, j, k) # [-1,0,3,5,9,12], 8
        if nums[k] < target:
            i = k + 1
        else:
            j = k
    return i if nums[i] == target else -1

def search2(nums: List[int], target: int) -> int:
    """不带等号写法：右边界"""
    n = len(nums)
    i, j = 0, n - 1
    while i < j:
        k = ((j - i + 1) >> 1) + i
        print(i, j, k) # [-1,0,3,5,9,12], 1
        if nums[k] > target:
            j = k - 1
        else:
            i = k
    return i if nums[i] == target else -1

def search3(nums: List[int], target: int) -> int:
    """终止条件：相邻元素，不推荐"""
    n = len(nums)
    i, j = 0, n - 1
    #目标元素可能存在在区间 [left, right]
    while i < j - 1: # i+i<j 或者 i=j-1等价上面v1,v2版本
        k = ((j - i) >> 1) + i
        if nums[k] == target:
            return k
        if nums[k] > target:
            j = k - 1
        if nums[k] < target:
            i = k + 1
    if nums[i] == target: return i
    if nums[j] == target: return j
    return -1

def main():
    param = [-1,0,3,5,9,12]
    ret = search3(param, 9)
    print(ret)

'''704. 二分查找

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
