#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """状态转移方程：
        0-1背包：dp[i][j] = max(dp[i−1][j], dp[i−1][j−w[i]]+v[i]) // j >= w[i]
        完全背包：dp[i][j] = max(dp[i−1][j], dp[i][j−w[i]]+v[i]) // j >= w[i]

        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        dp[i][j] = x 表示，对于前i个物品，当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，若x为false，则说明不能恰好将背包装满。
        """
        N = len(nums)
        W = sum(nums) // 2
        #奇数不可能划分为两个和相等的子集
        if sum(nums) % 2 == 1: return False
        if N * W == 0: return False
        #模板考虑了0的情况，这里不考虑，初始化要0行的值
        dp = [[False] * (W + 1) for _ in range(N + 1)]
        #初始化
        for i in range(N + 1):
            dp[i][0] = True
        #状态转移
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[N][W]

    def canPartition1(self, nums: List[int]) -> bool:
        """状态转移方程：
        0-1背包优化：dp[j] = max(dp[j], dp[j-w[j]]+v[j]) // 逆序枚举：状态有两个(v,w)，第i个物品依赖i-1的状态(顺序的话，当前数组前面的状态是加入i之后的状态)
        完全背包优化：dp[j] = max(dp[j], dp[j-w[j]]+v[j]) // 顺序枚举：直接符合
        dp[[j] = x 表示，当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，若x为false，则说明不能恰好将背包装满。
        """
        N = len(nums)
        W = sum(nums) // 2
        #奇数不可能划分为两个和相等的子集
        if sum(nums) % 2 == 1: return False
        if N * W == 0: return False
        #模板考虑了0的情况，这里不考虑，初始化要0行的值
        dp = [False] * (W + 1)
        #初始化
        dp[0] = True
        #状态转移：逆序枚举
        for i in range(0, N):
            for j in range(W, nums[i] - 1, -1):
                dp[j] = dp[j] | dp[j - nums[i]]
        print(dp)
        return dp[W]

def main():
    param = [1, 5, 11, 5]
    solution = Solution()
    ret = solution.canPartition(param)
    print(ret)
    ret = solution.canPartition1(param)
    print(ret)

'''416. 分割等和子集

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
