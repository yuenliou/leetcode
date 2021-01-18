#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        暴力优化2：消除一层循环+备忘录，超时，区分题122，含手续费 - fee
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
                maxPro = max(maxPro, dp(i+1) + prices[i] - prices[minIdx] - fee)
            memo[start] = maxPro
            return maxPro

        return dp(0)

    def maxProfit_dp(self, prices: List[int], fee: int) -> int:
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
        dp[0][1] = -prices[0] - fee

        for i in range(1, size):
            # 本题优化方程：k=1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        # print(dp)
        return dp[size - 1][0]

    def maxProfit_dp_s(self, prices: List[int], fee: int) -> int:
        """空间优化"""
        size = len(prices)
        if size <= 0: return 0

        #基本情况：
        dp_i_0 = 0
        dp_i_1 = -prices[0] - fee

        for i in range(1, size):
            # 本题优化方程：dp_i_1表示不含第i天的买入价
            new_dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            new_dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)
            dp_i_0 = new_dp_i_0
            dp_i_1 = new_dp_i_1
        return dp_i_0

def main():
    param = [1, 3, 2, 8, 4, 9]
    param2 = 2
    solution = Solution()
    ret = solution.maxProfit(param, param2)
    print(ret)

    ret = solution.maxProfit_dp(param, param2)
    print(ret)
    ret = solution.maxProfit_dp_s(param, param2)
    print(ret)


'''714. 买卖股票的最佳时机含手续费

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
