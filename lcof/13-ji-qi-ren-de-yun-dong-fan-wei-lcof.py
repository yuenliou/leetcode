#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """思路：向下，向右dfs。"""
        def sums(x):
            """数位和"""
            s = 0
            while x != 0:
                s += x % 10
                x = x // 10
            return s

        def dfs(i, j):
            if i >= m or j >= n or k < sums(i) + sums(j) or (i, j) in visited: return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i, j + 1)

        visited = set()
        return dfs(0, 0)


    def movingCount1(self, m: int, n: int, k: int) -> int:
        """
        思路：向下，向右dfs。数位和增量公式：s_x + 1 if (x + 1) % 10 else s_x - 8
        题解：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
        """

        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + \
                   dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount2(self, m: int, n: int, k: int) -> int:
        """BFS 实现： 通常利用队列实现广度优先遍历。初始将机器人初始点 (0, 0)(0,0) 加入队列 queue """
        queue, visited, = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)

    def movingCount3(self, m: int, n: int, k: int) -> int:
        """
        动态规划：搜索方向只需朝下或朝右，因此 (i, j) 的格子只会从 (i - 1, j) 或者 (i, j - 1) 两个格子走过来（不考虑边界条件），那么 vis[i][j] 是否可达的状态则可由如下公式计算得到：
        状态转移方程：vis[i][j] = vis[i−1][j] or vis[i][j−1]
        """
        def sums(x):
            """数位和"""
            s = 0
            while x != 0:
                s += x % 10
                x = x // 10
            return s

        if k == 0: return 1
        ans = 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or sums(i) + sums(j) > k: continue
                if i - 1 >= 0: dp[i][j] |= dp[i - 1][j]
                if j - 1 >= 0: dp[i][j] |= dp[i][j - 1]
                ans += dp[i][j]
        print(dp)
        return ans

def main():
    param = 2
    param2 = 3
    param3 = 1
    solution = Solution()
    ret = solution.movingCount(param, param2, param3)
    print(ret)
    ret = solution.movingCount1(param, param2, param3)
    print(ret)
    ret = solution.movingCount2(param, param2, param3)
    print(ret)
    ret = solution.movingCount3(param, param2, param3)
    print(ret)

'''剑指 Offer 13. 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
