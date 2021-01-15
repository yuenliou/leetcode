#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def add(self, a: int, b: int) -> int:
        """思路：
        1.不给我们用四则运算，那就只能用位运算了
        2.不进位的和：异或，进位和：取余左移。然后相加(不能出现 + 就一直循环到进位和是0，最多32次)
        """
        x = 0xffffffff # -1
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

    def add1(self, a: int, b: int) -> int:
        """最多最多就是循环32次就行"""
        while b != 0:
            sum = a ^ b
            carry = (a & b) << 1
            a = sum
            b = carry
        return a

    def add2(self, a: int, b: int) -> int:
        """递归"""
        if b == 0: return a
        return self.add2(a ^ b, (a & b) << 1)

def main():
    param = 1
    param2 = -2
    solution = Solution()
    ret = solution.add(param, param2)
    print(ret)
    ret = solution.add1(param, param2)
    print(ret)
    ret = solution.add2(param, param2)
    print(ret)

'''剑指 Offer 65. 不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
