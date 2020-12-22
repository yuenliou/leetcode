#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """状态转移方程：0-1背包
        假设所有元素和为sum，所有添加正号的元素的和为A，所有添加负号的元素和为B，
        则有sum = A + B 且 S = A - B，解方程得A = (sum + S)/2。
        即题目转换成：从数组中选取一些元素使和恰好为(sum + S) / 2
        """
        N = len(nums)
        W = (sum(nums) + S) // 2
        #奇数不可能划分为两个和相等的子集
        if (sum(nums) + S) % 2 == 1: return 0
        if sum(nums) < S or sum(nums) < -S: return 0
        #dp数组
        dp = [0] * (W + 1)
        #初始化
        dp[0] = 1
        #状态转移：逆序枚举
        for i in range(1, N + 1):
            for j in range(W, nums[i - 1] - 1, -1):
                dp[j] = dp[j] + dp[j - nums[i - 1]]
            # print(dp)
        print(dp)
        return dp[W]

    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        """回溯算法：二进制递归枚举"""
        def backtrack(i, rest):
            nonlocal res
            # 终止返回结果：恰好凑出 target
            if i == len(nums):
                if rest == 0:
                    res += 1
                return

            # 给 nums[i] 选择 - 号
            rest += nums[i]
            # 穷举 nums[i + 1]
            backtrack(i + 1, rest)
            # 撤销选择
            rest -= nums[i]

            # 给 nums[i] 选择 + 号
            rest -= nums[i]
            # 穷举 nums[i + 1]
            backtrack(i + 1, rest)
            # 撤销选择
            rest += nums[i]

        res = 0
        backtrack(0, S)
        return res

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        """回溯算法：二进制递归枚举，优化消除重叠子问题
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485700&idx=1&sn=433fc5ec5e03a86064d458320332a688&chksm=9bd7f70caca07e1aad658333ac05df501796862a418d8f856b12bb6ca73a924552901ec86d9b&scene=21#wechat_redirect
        """
        def backtrack(i, rest):
            nonlocal res
            # 终止返回结果：恰好凑出 target
            if i == len(nums):
                return 1 if rest == 0 else 0
            # 查备忘录
            key = "{},{}".format(i, rest)
            if key in memo: return memo[key]
            # 穷举
            res = backtrack(i + 1, rest - nums[i]) + backtrack(i + 1, rest + nums[i])
            # 记入备忘录
            memo[key] = res
            return res

        res = 0
        memo = {}
        backtrack(0, S)
        return res

def main():
    param = [1, 1, 1, 1, 1]
    solution = Solution()
    ret = solution.findTargetSumWays(param, 3)
    print(ret)
    ret = solution.findTargetSumWays1(param, 3)
    print(ret)
    ret = solution.findTargetSumWays2(param, 3)
    print(ret)

'''494. 目标和

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
 

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
