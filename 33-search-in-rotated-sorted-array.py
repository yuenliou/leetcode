#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def search(nums: List[int], target: int) -> int:
    def findPivot(nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            # else:
                #无法区分左右区间，缩小区间right--，数组元素不重复的时候可以用
                # right -= 1
        return left

    if len(nums) == 0: return -1

    pivot = findPivot(nums)
    if nums[pivot] == target: #最小值
        return pivot
    elif nums[pivot] > target: #最小值还小，说明不存在
        return -1

    left, right = 0, len(nums) - 1

    if pivot != left and pivot != right: #升序/降序,旋转点是第一个，或者最后一个
        if nums[left] > target:
            left = pivot + 1
        else:
            right = pivot - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums[left] == target else -1

def main():
    param = [4,5,6,7,0,1,2]
    # param = [2,5,6,0,0,1,2]
    # param = [1,3]
    ret = search(param, 2)
    print(ret)

'''33. 搜索旋转排序数组

给你一个整数数组 nums ，和一个整数 target 。

该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

 
示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
 

提示：

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
