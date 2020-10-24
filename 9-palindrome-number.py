#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def isPalindrome(x: int) -> bool:
    # 考虑性能，特殊情况优先处理(这一行可以不用加)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    num = 0
    while x > num:# 直接判断一半就可以
        num = num * 10 + x % 10
        x //= 10
    return x == num or x == num // 10

def isPalindrome_v1(x: int) -> bool:
    """
    PS：会存在翻转溢出的问题
    :param x:
    :return:
    """
    y = x
    num = 0
    while (x > 0):
        mod = x % 10
        x //= 10
        num *= 10
        num += mod
    return num == y

def isPalindrome_str(x: int) -> bool:
    return str(x) == str(x)[::-1]

def main():
    num = 12321
    ret = isPalindrome(num)
    print(ret)


'''9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
