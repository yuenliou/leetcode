#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """带备忘录的递归算法：自顶向下"""
        def memoize(n):
            # 初始值
            if n == 0: return 0
            if n < 0: return -1
            # 查备忘录
            if n in cache: return cache[n]
            ans = float('inf')
            for coin in coins:
                # 子问题
                sub = memoize(n-coin)
                # 子问题无解
                if sub == -1: continue
                ans = min(ans, 1 + sub)
            # 备忘录
            cache[n] = ans if ans != float('INF') else -1
            return cache[n]

        cache = {}
        return memoize(amount)

    def coinChange1(self, coins: List[int], amount: int) -> int:
        """状态转移方程：动态规划：自下而上
        f(n) = 1 + min[f(n-coin)]，f0 = 0
        n: 目标金额，coin:硬币面值(coin属于集合coins)，n-coin:剩余面值，1:硬币个数
        """
        #dp 数组的定义：当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出。
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(1, len(dp)):
            # 内层 for 在求所有子问题 + 1 的最小值
            for coin in coins:
                # 子问题无解，硬币的面值大于最大值
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1

def main():
    param = [1, 2, 5]
    solution = Solution()
    ret = solution.coinChange(param, 11)
    print(ret)
    ret = solution.coinChange1(param, 11)
    print(ret)

'''322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
