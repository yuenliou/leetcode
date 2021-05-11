#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def int2binaryStr(self, n: int):
        """整型int到二进制字符串"""

        # binary = lambda x: '' if x == 0 else binary(x//2) + str(x%2)
        # return binary(n)

        # return bin(n).replace('0b', '')
        # return "{0:b}".format(n)

        res = ''
        while n:
            res += str(n % 2)
            n //= 2
        return res[::-1]
    def nOneOfInt(self, n: int):
        """二进制中1的个数"""
        m = 0
        while n:
            m += 1
            n = n & (n - 1)
        return m

    def nZeroOfInt(self, n: int):
        """二进制中0的个数"""
        m = 0
        flag = 1
        while n >= flag:
            if not (n & flag):
                m += 1
            flag = flag << 1
        return m

    def nZeroOfInt2(self, n: int):
        """8位二进制中0的个数：从左开始零的个数，遇到1就停止"""
        m = 0
        flag = 2 ** 7
        while flag:
            if n & flag: break
            m += 1
            flag = flag >> 1
        return m


def main():
    solution = Solution()
    ret = solution.int2binaryStr(10)
    print(ret)
    ret = solution.nOneOfInt(8)
    print(ret)
    ret = solution.nZeroOfInt(7)
    print(ret)
    ret = solution.nZeroOfInt2(16)
    print(ret)


if __name__ == '__main__':
    main()
