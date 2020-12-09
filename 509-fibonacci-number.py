#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def fib(self, N: int) -> int:
        """递归超时，记忆化递归实现(数组/哈希表)"""
        def memoize(N: int) -> int:
            if N <= 1: return N
            if N in self.cache.keys():
                return self.cache[N]
            self.cache[N] = memoize(N - 1) + memoize(N - 2)
            return memoize(N)
        self.cache = {0: 0, 1: 1}
        return memoize(N)

    def fib1(self, N: int) -> int:
        """递归(自上而下)超时，循环实现(自下而上)"""
        if N < 2: return N
        dp = [0] * (N + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, N + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]

    def fib2(self, N: int) -> int:
        """空间复杂度：O(1)"""
        if N < 2: return N
        a, b, sum = 0, 1, 0
        for _ in range(2, N + 1):
            sum = a + b
            a = b
            b = sum
        return sum

def main():
    param = 45
    solution = Solution()
    ret = solution.fib(param)
    print(ret)
    ret = solution.fib1(param)
    print(ret)
    ret = solution.fib2(param)
    print(ret)

'''509. 斐波那契数

斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 

提示：

0 ≤ N ≤ 30


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
