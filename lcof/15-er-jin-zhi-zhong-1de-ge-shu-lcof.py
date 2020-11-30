#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def hammingWeight(n: int) -> int:
    m = 0
    while n:
        m += 1
        n = n & (n - 1)
    return m

def hammingWeight2(n: int) -> int:
    m = 0
    flag = 1
    while n >= flag:
        if n & flag:
            m += 1
        flag = flag << 1
    return m

def hammingWeight1(n: int) -> int:
    m = 0
    while n:
        if n & 1:
            m += 1
        n = n >> 1
    return m

def main():
    """
    思路1.n >> 1然后和1做与运算，负数会导致无限循环
    思路2.1 << 1然后和n做与运算
    思路3.n & (n - 1) 每循环一次会把从右边开始的1置0
    """
    param = -11
    ret = hammingWeight(param)
    print(ret)

'''剑指 Offer 15. 二进制中1的个数

请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 

提示：

输入必须是长度为 32 的 二进制串 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
