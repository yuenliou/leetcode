#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """分析规律：贪心"""
        n = len(nums)
        if n <= 0: return 0
        nCurSum, nGreatestSum = 0, float('-inf')
        for i in range(n):
            if nCurSum <= 0:
                nCurSum = nums[i]
            else:
                nCurSum += nums[i]
            # print(nCurSum)
            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum
        return nGreatestSum

    def maxSubArray1(self, nums: List[int]) -> int:
        """状态转移方程：dp[i] 的值代表 nums 前 i 个数字的最大子数组和
        if nums[i] > nums[i-1], dp[i] = max(dp[i], dp[j] + 1)
        """
        # 条件检测
        n = len(nums)
        if n <= 0: return 0
        # 初始状态
        dp = nums
        #默认第一个数字
        ans = dp[0]
        # 状态转移
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i-1] + nums[i])
            # ans = max(dp)
            ans = max(ans, dp[i])
        print(dp)
        return ans

def main():
    param = [-2,1,-3,4,-1,2,1,-5,4]
    param = [-2,-3,-1,-5]
    solution = Solution()
    ret = solution.maxSubArray(param)
    print(ret)
    ret = solution.maxSubArray1(param)
    print(ret)

'''53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
