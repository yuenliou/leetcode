#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def replaceSpace(self, s: str) -> str:
        """考点：原来1个字符现在变成3个字符，空格后面的字符移动次数有重复"""
        c = 0
        for ch in s:
            c += 1 if ch == ' ' else 0

        #替换后的长度
        len1 = len(s) - 1
        len2 = len1 + c * 2
        charArr = [''] * (len2 + 1)

        #py/java字符串不可变，用数组模拟
        while len1 >= 0:
            if s[len1] == ' ':
                charArr[len2] = '0'
                len2 -= 1
                charArr[len2] = '2'
                len2 -= 1
                charArr[len2] = '%'
                len2 -= 1
            else:
                charArr[len2] = s[len1]
                len2 -= 1
            len1 -= 1

        return ''.join(charArr)

    def replaceSpace1(self, s: str) -> str:
        """正则替换：pythonic"""
        # return s.replace(" ", "%20")
        return ''.join(('%20' if c==' ' else c for c in s))

def main():
    param = "We are happy."
    solution = Solution()
    ret = solution.replaceSpace(param)
    print(ret)
    ret = solution.replaceSpace1(param)
    print(ret)

'''剑指 Offer 05. 替换空格

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
