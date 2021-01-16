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
