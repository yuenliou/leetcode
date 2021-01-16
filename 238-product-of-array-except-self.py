#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        优化循环次数：1层，双端同时遍历
        """
        size = len(nums)
        left = 1
        right = 1
        result = [1] * size

        for i in range(0, size):
            result[i] *= left
            # 持有左边的所有数的乘积
            left *= nums[i]
            result[size - i - 1] *= right
            # 持有左边的所有数的乘积
            right *= nums[size - i - 1]
        return result

def main():
    param = [2, 7, 11, 15]
    solution = Solution()
    ret = solution.productExceptSelf(param)
    print(ret)

'''238. 除自身以外数组的乘积

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
