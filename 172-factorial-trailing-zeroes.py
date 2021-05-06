#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        思路：问题转化成n分解成5的因子的个数，5
        """
        res = 0
        while n:
            n = n // 5
            res += n
        return res

def main():
    param = 125
    solution = Solution()
    ret = solution.trailingZeroes(param)
    print(ret)

'''172. 阶乘后的零

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
