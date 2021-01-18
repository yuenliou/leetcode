#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """模拟：奇偶和最大
        https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-by-ikaruga/
        """
        odd_sum = even_sum = 0
        for i in range(len(nums)):
            if i % 2:
                even_sum = max(even_sum, odd_sum)
                odd_sum += nums[i]
            else:
                odd_sum = max(even_sum, odd_sum)
                even_sum += nums[i]
        return max(odd_sum, even_sum)

    def rob1(self, nums: List[int]) -> int:
        """
        动态规划：每个房子有两种状态，选和不选
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        """
        size = len(nums)
        if size <= 0: return 0

        #初始化
        dp = [0] * (size + 1)

        #基本情况：
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, size + 1):
            # 状态转移方程
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # print(dp)
        return dp[size]

    def rob2(self, nums: List[int]) -> int:
        """动态规划空间优化"""
        size = len(nums)
        if size <= 0: return 0

        #基本情况：
        pre0 = 0
        pre = nums[0]
        curr = 0

        for i in range(2, size + 1):
            # 状态转移方程
            curr = max(pre, pre0 + nums[i - 1])
            pre0 = pre
            pre = curr
        return curr

def main():
    param = [1,2,3,1]
    param = [2,7,9,3,1]
    param = [2,1,1,2]
    solution = Solution()
    ret = solution.rob(param)
    print(ret)
    ret = solution.rob1(param)
    print(ret)
    ret = solution.rob2(param)
    print(ret)

'''198. 打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

0 <= nums.length <= 100
0 <= nums[i] <= 400


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
