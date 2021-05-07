#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        """
        思路：问题转化成n分解成5的因子的个数，5
        """
        #递归尾零个数
        def trailingZeroes(n):
            return n // 5 + trailingZeroes(n//5) if n > 0 else 0

        # 10 * K + 1 是个很宽泛的的上界，事实上这一题x <= 5*K+1 也是过。+1考虑0的情况
        lo, hi = K, 10 * K + 1
        while lo < hi:
            mi = (lo + hi) // 2
            zmi = trailingZeroes(mi)
            if zmi == K:
                return 5
            elif zmi < K:
                lo = mi + 1
            else:
                hi = mi
        return 0

def main():
    param = 125
    solution = Solution()
    ret = solution.preimageSizeFZF(param)
    print(ret)

'''793. 阶乘函数后 K 个零

 f(x) 是 x! 末尾是 0 的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）

例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。给定 K，找出多少个非负整数 x ，能满足 f(x) = K 。

 

示例 1：

输入：K = 0
输出：5
解释：0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。
示例 2：

输入：K = 5
输出：0
解释：没有匹配到这样的 x!，符合 K = 5 的条件。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
