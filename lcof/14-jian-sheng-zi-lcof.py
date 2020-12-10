#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import math

class Solution:
    def cuttingRope(self, n: int) -> int:
        """
        图解【暴力递归】【记忆化技术】【动态规划】【动态规划优化解法】【找规律】方法二：
        https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/xiang-jie-bao-li-di-gui-ji-yi-hua-ji-zhu-dong-tai-/
        """
        # 使用辅助函数helper
        def memoize(n):
            if n < 2: return 0
            if cache[n] != 0:
                return cache[n]
            for i in range(2, n):
                cache[n] = max(cache[n], max(i * (n - i), i * memoize(n - i)))
            return cache[n]

        cache = [0 for _ in range(n + 1)]
        return memoize(n)

    def cuttingRope1(self, n: int) -> int:
        """状态转移方程：
        特别地，0 不是正整数，1 是最小的正整数，0 和 1 都不能拆分，因此 dp[0]=dp[1]=0。
        当 i≥2 时，假设对正整数 i 拆分出的第一个正整数是 j（1≤j<i），则有以下两种方案：
        将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j×(i−j)；
        将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j×dp[i−j]。

        343.整数拆分：https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
        状态转移方程2：dp[i]=max(2×(i−2),2×dp[i−2],3×(i−3),3×dp[i−3])
        """
        #dp 数组的定义：当目标金额为 i 时，分成m段的最大乘积是dp[i]。
        if n < 2: return 0
        dp = [0] * (n+1)
        # 初始值
        # dp[1] = 1 #（m、n都是整数，n>1并且m>1）
        # dp[2], dp[3], dp[4], dp[5], dp[6] = 1, 2, 4, 6, 9

        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(2, len(dp)):
            # 内层 for 在求所有子问题 * j 的最大值
            for j in range(1, i):
                # 拆分一半就可以：2-6(j * (i - j))
                if j > i - j: continue
                # print(i, j, i - j)
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

    def cuttingRope2(self, n: int) -> int:
        """数学方法"""
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

def main():
    param = 10
    solution = Solution()
    ret = solution.cuttingRope(param)
    print(ret)
    ret = solution.cuttingRope1(param)
    print(ret)
    ret = solution.cuttingRope2(param)
    print(ret)

'''剑指 Offer 14- I. 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
