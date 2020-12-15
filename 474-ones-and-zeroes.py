#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """状态转移方程：0-1背包
        我们把每个字符串看做是一件物品，把字符串中0的数目和1的数目看做是两种“重量”，所以就变成了一个二维01背包问题，
        书包的两个限重分别是 m 和 n，要求书包能装下的物品的最大数目（也相当于价值最大，设每个物品价值为1）。
        """
        length = len(strs)
        #dp数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        #状态转移：逆序枚举
        for i in range(1, length + 1):
            # 初始化
            N = W = 0
            # 计算第i - 1个字符串的两个重量
            for c in strs[i - 1]:
                if c == '0': N += 1
                else: W += 1
            for j in range(m, N - 1, -1):
                for k in range(n, W - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - N][k - W] + 1)
                # print(dp)
        # print(dp)
        return dp[m][n]

def main():
    param = ["10", "0001", "111001", "1", "0"]
    solution = Solution()
    ret = solution.findMaxForm(param, 5, 3)
    print(ret)

'''474. 一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

 

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
 

提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ones-and-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
