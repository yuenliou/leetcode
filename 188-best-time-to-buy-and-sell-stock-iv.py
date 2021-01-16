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

def main():
    param = 2
    param2 = [7,1,2,3,6,4]
    param2 = [2, 4, 1]
    solution = Solution()
    ret = solution.maxProfit(param, param2)
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
