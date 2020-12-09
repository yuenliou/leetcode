#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:

    def fib(self, n: int) -> int:
        """0、1、1、2、3、5、8、13、21..."""
        if n < 2: return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib0(self, n: int) -> int:
        """递归超时，尾递归"""
        def fib_tail(n, a, b):
            if n < 2: return n
            if n == 2:
                return a + b
            else:
                return fib_tail(n-1, b, a+b)

        return fib_tail(n, 0, 1)

    def fib1(self, n: int) -> int:
        """递归超时，记忆化递归实现(数组/哈希表)"""
        def fibonacci(n, memo):
            # nonlocal memo
            if n < 2: return n
            if memo[0] != -1:
                return memo[n]
            else:
                memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
                return memo[n]
        #备忘录
        memo = [-1] * (n + 1)
        return fibonacci(n, memo)

    def fib2(self, n: int) -> int:
        """递归(自上而下)超时，循环实现(自下而上)"""
        if n < 2: return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def fib3(self, n: int) -> int:
        """递归(自上而下)超时，循环实现(自下而上)+优化O(1)"""
        if n < 2: return n
        pre, cur, sum = 0, 1, 0
        for _ in range(2, n + 1):
            sum = pre + cur
            pre = cur
            cur = sum
        return sum

    def fib4(self, n: int) -> int:
        """
        循环求余法：
        https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/mian-shi-ti-10-i-fei-bo-na-qi-shu-lie-dong-tai-gui/
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

def main():
    param = 30
    solution = Solution()
    ret = solution.fib0(param)
    print(ret) #明显卡顿
    ret = solution.fib1(param)
    print(ret)
    ret = solution.fib2(param)
    print(ret)
    ret = solution.fib3(param)
    print(ret)
    ret = solution.fib4(param)
    print(ret)

'''剑指 Offer 10- I. 斐波那契数列

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
