#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def numWays(self, n: int) -> int:
        """递归方程：f(n) = f(n-1) + f(n-2)，n >= 2"""
        if n < 2: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1000000007

    def numWays1(self, n: int) -> int:
        """空间复杂度：O(1)"""
        if n < 2: return n
        a, b, sum = 1, 1, 0
        for _ in range(2, n + 1):
            sum = a + b
            a = b
            b = sum
        return sum % 1000000007

def main():
    param = 7
    solution = Solution()
    ret = solution.numWays(param)
    print(ret)
    ret = solution.numWays1(param)
    print(ret)

'''剑指 Offer 10- II. 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1

提示：

0 <= n <= 100
注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
