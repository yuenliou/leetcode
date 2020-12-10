#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """状态转移方程：自顶向下
        dp[m][n] = dp[m][n-1] + dp[m-1][n]
        """
        def memoize(i, j):
            # 初始值
            if i == 0: return 1
            if j == 0: return 1
            # 查备忘录
            if cache[i][j] != 0:
                return cache[i][j]
            # 求解子问题
            cache[i][j] = memoize(i, j - 1) + memoize(i - 1, j)
            # print(i, j, cache[i][j], cache)
            return cache[i][j]

        if m <= 0 or n <= 0: return 0

        #注意行列顺序
        cache = [[0 for _ in range(n)] for _ in range(m)]
        return memoize(m - 1, n - 1)

    def uniquePaths1(self, m: int, n: int) -> int:
        """状态转移方程：自底向上
        dp[m][n] = dp[m][n-1] + dp[m-1][n]
        """
        # 条件判断
        if m <= 0 or n <= 0: return 0

        # 初始化
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m): dp[i][0] = 1
        for j in range(n): dp[0][j] = 1

        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        print(dp)
        return dp[m-1][n-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        """状态转移方程2：自底向上，优化至一维数组：(i-1,j-1)只依赖前一行和当前行前一个元素的值
        dp[i] = dp[i-1] + dp[i]
        """
        # 条件判断
        if m <= 0 or n <= 0: return 0

        # 初始化(1行，所以用列n的值)
        dp = [0 for _ in range(n)]
        for i in range(n): dp[i] = 1

        # 状态转移
        for i in range(1, m):
            # dp[0] = 1
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
            print(dp)
        # print(dp)
        return dp[n-1]

def main():
    param = 3
    param2 = 7
    solution = Solution()
    ret = solution.uniquePaths(param, param2)
    print(ret)
    ret = solution.uniquePaths1(param, param2)
    print(ret)
    ret = solution.uniquePaths2(param, param2)
    print(ret)

'''62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
