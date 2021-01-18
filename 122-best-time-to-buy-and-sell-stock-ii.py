#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        暴力思路：无效for...for嵌套转化为递归
        """
        size = len(prices)
        if size <= 0: return 0

        maxPro = 0
        for i in range(size):
            for j in range(i+1, size):
                maxPro = max(maxPro, self.maxProfit(prices[j+1:]) + prices[j] - prices[i])
        return maxPro

    def maxProfit1(self, prices: List[int]) -> int:
        """
        暴力优化：消除一层循环+备忘录
        """
        size = len(prices)
        if size <= 0: return 0

        minIdx = 0
        maxPro = 0
        for i in range(1, size):
            if prices[i] < prices[minIdx]:
                minIdx = i
            maxPro = max(maxPro, self.maxProfit1(prices[i+1:]) + prices[i] - prices[minIdx])
        return maxPro

    def maxProfit2(self, prices: List[int]) -> int:
        """
        暴力优化2：消除一层循环+备忘录
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
                maxPro = max(maxPro, dp(i+1) + prices[i] - prices[minIdx])
            memo[start] = maxPro
            return maxPro

        return dp(0)

    def maxProfit3(self, prices: List[int]) -> int:
        """
        贪心思想：固定卖出时间，既然可以预知未来，那么能赚一点就赚一点
        """
        size = len(prices)
        if size <= 0: return 0

        maxPro = 0
        for i in range(1, size):
            if prices[i] > prices[i-1]:
                maxPro = maxPro + prices[i] - prices[i-1]
        return maxPro

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
            # 本题优化方程：k=inf
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]- prices[i])
        # print(dp)
        return dp[size - 1][0]

    def maxProfit_dp_s(self, prices: List[int]) -> int:
        """空间优化"""
        size = len(prices)
        if size <= 0: return 0

        #基本情况：
        dp_i_0 = 0
        dp_i_1 = float('-inf')

        for i in range(1, size):
            # 本题优化方程：dp_i_0表示含第i天的卖出价，dp_i_1表示不含第i天的买入价
            new_dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            new_dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
            dp_i_0 = new_dp_i_0
            dp_i_1 = new_dp_i_1
        return dp_i_0

def main():
    param = [7,1,5,3,6,4]
    param = [7,1,2,3,6,4]
    solution = Solution()
    ret = solution.maxProfit(param)
    print(ret)
    ret = solution.maxProfit1(param)
    print(ret)
    ret = solution.maxProfit2(param)
    print(ret)
    ret = solution.maxProfit3(param)
    print(ret)

    ret = solution.maxProfit_dp(param)
    print(ret)
    ret = solution.maxProfit_dp_s(param)
    print(ret)

'''122. 买卖股票的最佳时机 II

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
