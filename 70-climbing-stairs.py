#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def climbStairs(self, n: int) -> int:
        """递归方程：f(n) = f(n-1) + f(n-2)，n >= 2"""
        if n < 2: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs1(self, n: int) -> int:
        """空间复杂度：O(1)"""
        if n < 2: return n
        a, b, sum = 1, 1, 0
        for _ in range(2, n + 1):
            sum = a + b
            a = b
            b = sum
        return sum

def main():
    param = 7
    solution = Solution()
    ret = solution.climbStairs(param)
    print(ret)
    ret = solution.climbStairs1(param)
    print(ret)

'''70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
