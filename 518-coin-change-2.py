#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        """状态转移方程：
        0-1背包：dp[i][j] = max(dp[i−1][j], dp[i−1][j−w[i]]+v[i]) // j >= w[i]
        完全背包：dp[i][j] = max(dp[i−1][j], dp[i][j−w[i]]+v[i]) // j >= w[i]
        两种情况区别：状态转移dp[i−1][j−w[i]] => dp[i][j−w[i]]，即装入第i种商品后还可以再继续装入第种商品。

        https://zhuanlan.zhihu.com/p/93857890
        最基本的背包问题就是01背包问题（01 knapsack problem）：
        一共有N件物品，第i（i从1开始）件物品的重量为w[i]，价值为v[i]。在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？

        dp[i][j]表示将前i件物品装进限重为j的背包可以获得的最大价值, 0<=i<=N, 0<=j<=W。
        base case 就是dp[0][..] = dp[..][0] = 0，因为没有物品或者背包没有空间的时候，能装的最大价值就是 0。

        ```
        #0-1背包两层循环
        for i in range(1, N+1):
            for j in range(1, W+1):
                #j表示剩余可用容量，w[i-1]表示第i个物品重量
                if j >= w[i-1]:
                    #当前物品价值 + 取当前物品后的剩余空间
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
                else:
                    #物品i放不下，继承上一个物品的最大值。
                    dp[i][j] = dp[i-1][j]
        ```
        ```
        #完全背包第三层循环，或者两层也可以
        for...for...
            for k in range(j//w[i]+1):
                # 枚举下标为 i 的物品可以选的个数
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-k*w[i-1]] + v[i-1]*k)
        ```
        """
        N = len(coins)
        W = amount
        if W == 0: return 1
        if N * W == 0: return 0
        #模板考虑了0的情况，这里不考虑，初始化要0行的值
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        #初始化
        for i in range(N + 1):
            dp[i][0] = 1
        #状态转移(三层循环：上一行的初始状态)
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                # 枚举下标为 i 的物品可以选的个数
                for k in range(j // coins[i - 1] + 1):
                    # print(i, j, k, i - 1, j - k * coins[i - 1])
                    dp[i][j] += dp[i - 1][j - k * coins[i - 1]]
        print(dp)
        return dp[N][W]

    def change1(self, amount: int, coins: List[int]) -> int:
        """两层循环"""
        N = len(coins)
        W = amount
        if W == 0: return 1
        if N * W == 0: return 0
        #模板考虑了0的情况，这里不考虑，初始化要0行的值
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        #初始化
        for i in range(N + 1):
            dp[i][0] = 1
        #状态转移(两层循环：当前行第一列的初始状态)
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if j >= coins[i - 1]:
                    # print(i, j, i, j - coins[i - 1])
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[N][W]

def main():
    param = [1, 2, 5]
    solution = Solution()
    ret = solution.change(5, param)
    print(ret)
    # param = [2]
    ret = solution.change1(5, param)
    print(ret)

'''518. 零钱兑换 II

给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10] 
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
