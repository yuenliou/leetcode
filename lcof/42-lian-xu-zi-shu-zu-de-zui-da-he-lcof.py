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
    # param = [-2,-3,-1,-5]
    solution = Solution()
    ret = solution.maxSubArray(param)
    print(ret)
    ret = solution.maxSubArray1(param)
    print(ret)

'''剑指 Offer 42. 连续子数组的最大和

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
