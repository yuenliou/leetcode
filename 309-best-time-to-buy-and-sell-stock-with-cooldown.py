#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        暴力优化2：消除一层循环+备忘录，区分题122，dp(i+1)有个冷静期
        """
        size = len(prices)
        if size <= 0: return 0

        memo = [-1] * size
        def dp(start):
            if start >= size: return 0
            if memo[start] != -1: return memo[start]

            minIdx = start
            maxPro = 0
            for i in range(start + 1, size):
                if prices[i] < prices[minIdx]:
                    minIdx = i
                maxPro = max(maxPro, dp(i+2) + prices[i] - prices[minIdx])
            memo[start] = maxPro
            return maxPro

        return dp(0)

    def maxProfit_dp(self, prices: List[int]) -> int:
        """
        动态规划：三个操作状态buy, sell, rest。
        通用状态转移方程：s[0,1]两种(有无股票)状态的两种情况，昨天的股票持有状态和今天的操作影响今天的收益情况
        dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    = max(继承前一天rest, 当天选择sell)
        dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                    = max(继承前一天rest, (上个交易日最大值-)当天选择buy)
        基本情况：
        dp[-1][k][0] = 0 # 没开始无股票的最大收益
        dp[-1][k][1] = -Infinity # 没开始有股票的最大收益
        dp[i][0][0] = 0 # 已开始无交易无股票的最大收益
        dp[i][0][1] = -Infinity # 已开始无交易有股票的最大收益

        labuladong团灭系列：https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484508&idx=1&sn=42cae6e7c5ccab1f156a83ea65b00b78&chksm=9bd7fa54aca07342d12ae149dac3dfa76dc42bcdd55df2c71e78f92dedbbcbdb36dec56ac13b&scene=21#wechat_redirect
        股票问题系列通解（转载翻译）：https://leetcode-cn.com/circle/article/qiAgHn/
        """

        size = len(prices)
        if size <= 0: return 0

        #初始化
        dp = [[0] * 2 for _ in range(size)]

        #基本情况：
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, size):
            # 本题优化方程：k=inf+cooldown
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], (dp[i - 2][0] if i >= 2 else 0) - prices[i])
        # print(dp)
        return dp[size - 1][0]

    def maxProfit_dp_s(self, prices: List[int]) -> int:
        """空间优化"""
        size = len(prices)
        if size <= 0: return 0

        #基本情况：
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        dp_pre_0 = 0 #dp[i - 2][0]

        for i in range(1, size):
            # 本题优化方程：dp_i_0表示含第i天的卖出价，dp_i_1表示不含第i天的买入价
            new_dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            new_dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
            dp_i_0 = new_dp_i_0
            dp_i_1 = new_dp_i_1
        return dp_i_0

def main():
    param = [1,2,3,0,2]
    solution = Solution()
    ret = solution.maxProfit(param)
    print(ret)

    ret = solution.maxProfit_dp(param)
    print(ret)
    ret = solution.maxProfit_dp_s(param)
    print(ret)

'''309. 最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
