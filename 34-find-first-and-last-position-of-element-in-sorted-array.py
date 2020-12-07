#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # print(left, right, mid)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            # print(left, right, mid)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return right if nums[right] == target else -1

    if len(nums) == 0: return [-1, -1]
    i = findLeft(nums, target)
    if i == -1: return [-1, -1]
    j = findRight(nums, target)
    return [i, j]

def main():
    param = [5,7,7,8,8,8,8,8,10]
    ret = searchRange(param, 8)
    print(ret)

'''34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
