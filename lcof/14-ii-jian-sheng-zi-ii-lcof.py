#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import math

class Solution:
    def cuttingRope(self, n: int) -> int:
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
        return dp[n] % 1000000007
def main():
    param = 10
    solution = Solution()
    ret = solution.cuttingRope(param)
    print(ret)

'''剑指 Offer 14- II. 剪绳子 II
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 

提示：

2 <= n <= 1000
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
