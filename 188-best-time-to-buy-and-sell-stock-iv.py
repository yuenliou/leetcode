#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        暴力优化2：消除一层循环+备忘录，超时90分吧，后续状态机优化
        """
        size = len(prices)
        if size <= 0: return 0

        memo = {}
        def dp(start, k):
            if k == 0: return 0
            if start >= size: return 0
            if (start, k) in memo: return memo[(start, k)]

            minIdx = start
            maxPro = 0
            for i in range(start + 1, size):
                if prices[i] < prices[minIdx]:
                    minIdx = i
                maxPro = max(maxPro, dp(i+1, k-1) + prices[i] - prices[minIdx])
            memo[(start, k)] = maxPro
            return maxPro

        return dp(0, k)

    def maxProfit_dp(self, k: int, prices: List[int]) -> int:
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
        dp = [[[0] * 2 for _ in range(k + 1)]for _ in range(size)]

        #基本情况：
        for j in range(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, size):
            # 本题优化方程：k=inf，枚举k，注意k--，k++都可以
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        # print(dp)
        return dp[size - 1][k][0]

    def maxProfit_dp_s(self, k: int, prices: List[int]) -> int:
        """空间优化"""
        size = len(prices)
        if size <= 0: return 0

        def maxProfit_dp_inf(prices: List[int]):
            # 初始化
            dp = [[0] * 2 for _ in range(size)]

            # 基本情况：
            dp[0][0] = 0
            dp[0][1] = -prices[0]

            for i in range(1, size):
                # 本题优化方程：k=inf
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # print(dp)
            return dp[size - 1][0]

        #k没有意义拓展成无穷大，同题122
        if k > size // 2:
            return maxProfit_dp_inf(prices)

        #初始化
        dp = [[[0] * 2 for _ in range(k + 1)]for _ in range(size)]

        #基本情况：
        for j in range(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, size):
            # 本题优化方程：k=inf，枚举k，注意k--，k++都可以
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        # print(dp)
        return dp[size - 1][k][0]

def main():
    param = 2
    # param2 = [7,1,2,3,6,4]
    param2 = [2, 4, 1]
    # param2 = [3,2,6,5,0,3]
    solution = Solution()
    ret = solution.maxProfit(param, param2)
    print(ret)

    ret = solution.maxProfit_dp(param, param2)
    print(ret)
    ret = solution.maxProfit_dp_s(param, param2)
    print(ret)

'''188. 买卖股票的最佳时机 IV

给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 

提示：

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
