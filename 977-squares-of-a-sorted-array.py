#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List


def sortedSquares(A: List[int]) -> List[int]:
    n = len(A)
    ans = [0] * n

    i, j, pos = 0, n - 1, n - 1
    while i <= j:
        if A[i] * A[i] > A[j] * A[j]:
            ans[pos] = A[i] * A[i]
            i += 1
        else:
            ans[pos] = A[j] * A[j]
            j -= 1
        pos -= 1

    return ans

def main():
    a = [-4,-1,0,3,10]
    ret = sortedSquares(a)
    print(ret)

    b = [-7,-3,2,3,11]
    ret = sortedSquares(b)
    print(ret)

'''977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
