#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        贪心思想：固定了买入时间 vs 固定卖出时间
        动态规划：dp[i]为卖出价是数组中第i个数字的最大利润，显然找出i-1中的最小值就可以了
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484509&idx=1&sn=21ace57f19d996d46e82bd7d806a2e3c&source=41#wechat_redirect
        """
        size = len(prices)
        if size <= 0: return 0

        minIdx = 0
        maxPro = 0
        for i in range(1, size):
            if prices[i] < prices[minIdx]:
                minIdx = i
            maxPro = max(maxPro, prices[i] - prices[minIdx])
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
            # 本题优化方程：k=1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
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
            # 本题优化方程：dp_i_1表示不含第i天的买入价
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])
        return dp_i_0

def main():
    param = [7,1,5,3,6,4]
    solution = Solution()
    ret = solution.maxProfit(param)
    print(ret)

    ret = solution.maxProfit_dp(param)
    print(ret)
    ret = solution.maxProfit_dp_s(param)
    print(ret)

'''121. 买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
