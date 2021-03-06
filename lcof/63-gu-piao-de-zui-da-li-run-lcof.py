#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        直接解法：[2,4,1]不满足
        """
        size = len(prices)
        if size <= 0: return 0

        minIdx = 0
        for i in range(1, size):
            if prices[i] < prices[minIdx]:
                minIdx = i

        maxPro = 0
        for i in range(minIdx + 1, size):
            maxPro = max(maxPro, prices[i] - prices[minIdx])
        return maxPro

    def maxProfit1(self, prices: List[int]) -> int:
        """
        暴力解法：超时，遍历每一个数对，固定了买入时间
        改变思路：上述前面2，4也符合但是没有计算，暴力，把每个数都当成最小值，然后计算和最大值的差别
        """
        size = len(prices)
        if size <= 0: return 0

        maxPro = 0
        for i in range(size):
            for j in range(i+1, size):
                maxPro = max(maxPro, prices[j] - prices[i])
        return maxPro

    def maxProfit2(self, prices: List[int]) -> int:
        """
        贪心思想：固定卖出时间
        动态规划：dp[i]为卖出价是数组中第i个数字的最大利润，显然找出i-1中的最小值就可以了
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

def main():
    param = [7,1,5,3,6,4]
    # param = [7,6,4,3,1]
    # param = [2,4,1]
    solution = Solution()
    ret = solution.maxProfit(param)
    print(ret)
    ret = solution.maxProfit1(param)
    print(ret)
    ret = solution.maxProfit2(param)
    print(ret)

'''剑指 Offer 63. 股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5

 

注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
