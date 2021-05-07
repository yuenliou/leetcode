#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def _nextGreaterElement(self, nums: List[int]) -> List[int]:
        """
        思路1：暴力解
        思路2：单调栈 [2,1,2,4,3]
        """
        res = [0] * len(nums)
        stack = []
        # 倒着往栈里放
        for i in range(len(nums) - 1, -1, -1):
            # 维护了一个 递增栈
            while len(stack) and stack[-1] <= nums[i]:
                stack.pop()
            # nums[i] 身后的 next great number
            if len(stack):
                res[i] = stack[-1]
            else:
                res[i] = -1
            stack.append(nums[i])
        return res

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        思路1：暴力解
        思路2：单调栈 [2,1,2,4,3]
        作文题：No, it's asking you to take an element in the first array and then find the same element in the second array and then look to the right in the second array to find a greater one. I couldn`t understand this until I looked into some solutions in the discussi
        """
        res = [0] * len(nums1)
        stack = []
        map = {}
        # 先处理 nums2，把对应关系存入哈希表
        for i in range(len(nums2)):
            while len(stack) and stack[-1] < nums2[i]:
                map[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        # 遍历 nums1 得到结果集
        for i in range(len(nums1)):
            res[i] = map[nums1[i]] if nums1[i] in map else -1
        return res

def main():
    # param = [4, 1, 2]
    # param2 = [1, 3, 4, 2]
    param = [3, 1, 2]
    param2 = [1, 3, 2, 4]
    solution = Solution()
    ret = solution._nextGreaterElement([2, 1, 2, 4, 3])
    print(ret)
    ret = solution.nextGreaterElement(param, param2)
    print(ret)


'''496. 下一个更大元素 I

给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

 

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
 

提示：

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中
 

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
