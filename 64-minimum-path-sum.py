#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """状态转移方程：自顶向下
        dp[m][n] = min(dp[m][n-1], dp[m-1][n]) + grid[i][j]
        """
        def memoize(i, j):
            # 初始值
            if i == 0 or j == 0: return cache[i][j]
            # 查备忘录
            if cache[i][j] != 0:
                return cache[i][j]
            # 求解子问题
            cache[i][j] = min(memoize(i, j - 1), memoize(i - 1, j)) + grid[i][j]
            # print(i, j, cache[i][j], cache)
            return cache[i][j]

        #注意行列顺序
        m, n = len(grid), len(grid[0])
        if m <= 0 or n <= 0: return 0
        cache = [[0 for _ in range(n)] for _ in range(m)]

        #缓存初始值
        cache[0][0] = grid[0][0]
        for i in range(1, m): cache[i][0] = cache[i-1][0] + grid[i][0]
        for j in range(1, n): cache[0][j] = cache[0][j-1] + grid[0][j]

        return memoize(m - 1, n - 1)

    def minPathSum1(self, grid: List[List[int]]) -> int:
        """状态转移方程：自底向上
        dp[m][n] = min(dp[m][n-1], dp[m-1][n]) + grid[i][j]
        """
        m, n = len(grid), len(grid[0])
        if m <= 0 or n <= 0: return 0

        # 初始化
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]

        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                # print(dp[i][j-1], dp[i-1][j], grid[i][j], min(dp[i][j-1], dp[i-1][j]) + grid[i][j])
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        print(dp)
        return dp[m-1][n-1]

    def minPathSum2(self, grid: [[int]]) -> int:
        """状态转移方程2：自底向上，优化至一维数组：(i-1,j-1)只依赖前一行和当前行前一个元素的值
        dp[i] = min(dp[i-1], dp[i]) + grid[i][j]
        """
        # 条件判断
        m, n = len(grid), len(grid[0])
        if m <= 0 or n <= 0: return 0

        # 初始化(1行，所以用列n的值)
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for i in range(1, n): dp[i] = dp[i-1] + grid[0][i]

        # 状态转移
        for i in range(1, m):
            # 第 i 行第 0 列的初始值：【重点】
            dp[0] = 0
            for k in range(0, i + 1): dp[0] += grid[k][0]

            for j in range(1, n):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
            print(dp)
        # print(dp)
        return dp[n-1]

    def minPathSum3(self, grid: [[int]]) -> int:
        """优化：直接用原数组grid操作"""
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

def main():
    param = [[1,3,1],[1,5,1],[4,2,1]]
    solution = Solution()
    ret = solution.minPathSum(param)
    print(ret)
    ret = solution.minPathSum1(param)
    print(ret)
    ret = solution.minPathSum2(param)
    print(ret)
    ret = solution.minPathSum3(param)
    print(ret)

'''64. 最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
