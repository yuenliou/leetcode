#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def isNumber(self, s: str) -> bool:
        """剑指Offer思路：
        数字的格式可以用A[.[B]][e|EC]或者.B[e|EC]表示，
        其中A和C都是整数（可以有正负号，也可以没有），而B是一个无符号整数
        """
        s = s.strip()
        if not s: return False

        def scanInteger():
            nonlocal start
            if start < len(s) and s[start] in ['+', '-']:
                start += 1
            return scanUnsignedInteger()

        def scanUnsignedInteger():
            nonlocal start
            flag = False
            while start < len(s) and s[start] >= '0' and s[start] <= '9':
                flag = True
                start += 1
            return flag

        start = 0

        # 整数部分
        numeric = scanInteger()

        # 小数部分
        if start < len(s) and s[start] == '.':
            start += 1
            #顺序不能乱，防止短路numeric or scanUnsignedInteger()
            numeric = scanUnsignedInteger() or numeric

        # 指数部分
        if start < len(s) and (s[start] == 'e' or s[start] == 'E'):
            start += 1
            numeric = scanInteger() and numeric

        return numeric and start == len(s)

def main():
    #True
    param = '+100'
    param = '5e2'
    param = '-123'
    param = '3.1416'
    param = '-1E-16'
    param = '0123'
    param = '0.8'
    #False
    # param = '12e'
    # param = '1a3.14'
    # param = '1.2.3'
    # param = '+-5'
    # param = '12e+5.4'
    solution = Solution()
    ret = solution.isNumber(param)
    print(ret)

'''剑指 Offer 20. 表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
