#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import collections

class Solution:
    def firstUniqChar(self, s: str) -> str:
        """26位数组"""
        ch2idx = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            ch2idx[idx] += 1
        # print(ch2idx)
        for ch in s:
            idx = ord(ch) - ord('a')
            if ch2idx[idx] == 1: return chr(idx + 97)
        return ' '

    def firstUniqChar1(self, s: str) -> str:
        """字典： Map 结构的 Value 使用 Boolean 类型， 1.简化判断，2去除int的递增"""
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '

    def firstUniqChar2(self, s: str) -> str:
        """有序字典"""
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '

def main():
    param = "abaccdeff"
    solution = Solution()
    ret = solution.firstUniqChar(param)
    print(ret)
    ret = solution.firstUniqChar1(param)
    print(ret)
    ret = solution.firstUniqChar2(param)
    print(ret)

'''剑指 Offer 50. 第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
 

限制：

0 <= s 的长度 <= 50000



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
