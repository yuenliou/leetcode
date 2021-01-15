#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        """计算方法主要有三种：平均计算、迭代、递归"""
        #逻辑运算符的短路效应：递归if优化版本
        # 当 n = 1 时 n > 1 不成立 ，此时 “短路” ，终止后续递归
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res

    def sumNums1(self, n):
        """不满足"""
        if n == 1: return 1
        n += self.sumNums1(n - 1)
        return n

    def sumNums2(self, n):
        """递归+短路"""
        return n and n + self.sumNums2(n - 1)

def main():
    param = 3
    solution = Solution()
    ret = solution.sumNums(param)
    print(ret)
    ret = solution.sumNums1(param)
    print(ret)
    ret = solution.sumNums2(param)
    print(ret)

'''剑指 Offer 64. 求1+2+…+n

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
