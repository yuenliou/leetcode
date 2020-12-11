#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """带备忘录的递归算法：自顶向下
        递归+动态规划+二分：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/chao-xiang-xi-tu-jie-di-gui-dong-tai-gui-hua-er-fe/
        """
        def memoize(i):
            # 边界条件
            if i == 0: return 1
            # 查缓存
            if cache[i] != 0:
                return cache[i]
            # 求解子问题
            cache[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    # RecursionError: maximum recursion depth exceeded in comparison
                    # dp[i] = max(dp[i], dp[0..i] + 1)
                    cache[i] = max(cache[i], memoize(j) + 1)
            return cache[i]

        n = len(nums)
        if n <= 0: return 0

        cache = [0] * n
        cache[0] = 1
        # ans = memoize(n - 1)
        ans = 1
        for i in range(n):
            ans = max(ans, memoize(i))
        print(cache)
        return ans

    def lengthOfLIS1(self, nums: List[int]) -> int:
        """状态转移方程：dp[i] 的值代表 nums 前 i 个数字的最长子序列长度
        if nums[i] > nums[i-1], dp[i] = max(dp[i], dp[j] + 1)
        """
        # 条件检测
        n = len(nums)
        if n <= 0: return 0
        # 初始状态
        dp = [1] * n
        #默认第一个是最长的上升子序列的长度
        ans = dp[0]
        # 状态转移：推导-对于i,前面有几个比i小的数，既最长上升子序列的长度（对于当前i，后面有几个比i大的数，没发现规律）
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(dp)
        print(dp)
        return ans

def main():
    param = [10,9,2,5,3,7,101,18]
    # param = [4,10,4,3,8,9]

    solution = Solution()
    ret = solution.lengthOfLIS(param)
    print(ret)
    ret = solution.lengthOfLIS1(param)
    print(ret)

'''300. 最长上升子序列

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
