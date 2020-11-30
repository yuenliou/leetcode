#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def printNumbers(n: int) -> List[int]:
    def dfs(x):
        # https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
        nonlocal start, nine
        if x == n:
            s = ''.join(num[start:])
            if s != '0': res.append(int(s))
            if n - start == nine: start -= 1
            return
        for i in range(10):
            if i == 9: nine += 1
            num[x] = str(i)
            dfs(x + 1)
        nine -= 1

    num, res = ['0'] * n, []
    nine = 0
    start = n - 1
    dfs(0)
    return res

def printNumbers1(n: int) -> List[int]:
    res = []
    for i in range(pow(10, n)-1):
        res.append(i+1)
    # return list(range(1, 10 ** n))
    return res

def main():
    """
    思路1.直接遍历1-10的n次方-1，会有溢出问题，采用大数思维(字符串或者数组)
    思路2.字符串递归全排列
    """
    param = 2
    ret = printNumbers(param)
    print(ret)

'''剑指 Offer 17. 打印从1到最大的n位数

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
