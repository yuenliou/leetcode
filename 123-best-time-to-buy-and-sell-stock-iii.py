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
        dp = [[[0] * 2 for _ in range(3)]for _ in range(size)]

        #基本情况：
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]

        for i in range(1, size):
            # 本题优化方程：k=2,穷举4种情况,也可用for参考188题
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
            # dp[i][1][1] = max(dp[i - 1][1][1], - prices[i])
        # print(dp)
        return dp[size - 1][2][0]

    def maxProfit_dp_s(self, k: int, prices: List[int]) -> int:
        """空间优化"""
        size = len(prices)
        if size <= 0: return 0

        #基本情况：
        dp_i_10 = 0
        dp_i_11 = -prices[0]
        dp_i_20 = 0
        dp_i_21 = -prices[0]

        for i in range(1, size):
            # 本题优化方程：dp_i_0表示含第i天的卖出价，dp_i_1表示不含第i天的买入价
            dp_i_20 = max(dp_i_20, dp_i_21 + prices[i])
            dp_i_21 = max(dp_i_21, dp_i_10- prices[i])
            dp_i_10 = max(dp_i_10, dp_i_11 + prices[i])
            dp_i_11 = max(dp_i_11, - prices[i])
        return dp_i_20

def main():
    param = 2
    param2 = [7,1,2,3,6,4]
    param2 = [3,3,5,0,0,3,1,4]
    param2 = [1,2,3,4,5]
    solution = Solution()
    ret = solution.maxProfit(param, param2)
    print(ret)

    ret = solution.maxProfit_dp(param, param2)
    print(ret)
    ret = solution.maxProfit_dp_s(param, param2)
    print(ret)


'''123. 买卖股票的最佳时机 III

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：

输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：

输入：prices = [1]
输出：0
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
