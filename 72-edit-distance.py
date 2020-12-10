#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import functools

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """带备忘录的递归算法：自顶向下
        自底向上和自顶向下：https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
        """
        # @functools.lru_cache(None)
        def memoize(i, j):
            # 边界条件
            if i == -1: return j + 1
            if j == -1: return i + 1
            # 查缓存
            if cache[i][j] != 0:
                return cache[i][j]
            # 求解子问题
            if word1[i] == word2[j]:
                cache[i][j] = memoize(i - 1, j - 1)
                return cache[i][j]
            else:
                cache[i][j] = min(memoize(i, j - 1), memoize(i - 1, j), memoize(i - 1, j - 1)) + 1
                return cache[i][j]

        n1, n2 = len(word1), len(word2)
        cache = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        return memoize(n1 - 1, n2 - 1)

    def minDistance1(self, word1: str, word2: str) -> int:
        """状态转移方程：
        当字符串 word1 的长度为 i，字符串 word2 的长度为 j 时，将 word1 转化为 word2 所使用的最少操作次数
        动图参考(第6秒)：https://leetcode-cn.com/problems/edit-distance/solution/edit-distance-by-ikaruga/
        官方还是更胜一筹：https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
        状态理解&同类问题：https://leetcode-cn.com/problems/edit-distance/solution/dong-tai-gui-hua-java-by-liweiwei1419/
        dp[i][j] 代表 word1 中第 i 个字符，变换到 word2 中第 j 个字符，最短需要操作的次数
        需要考虑 word1 或 word2 一个字母都没有，即全增加/删除的情况，所以预留 dp[0][j] 和 dp[i][0]
        特例相同时：word1[i - 1] = word2[j - 1] ，dp[i][j] = dp[i - 1][j - 1]
        增，dp[i][j] = dp[i][j - 1] + 1。理解：word1不动，word2删除一个字符
        删，dp[i][j] = dp[i - 1][j] + 1。理解：word1删除一个字符与word2相等
        改，dp[i][j] = dp[i - 1][j - 1] + 1
        """
        n1 = len(word1)
        n2 = len(word2)
        # +1兼容空字符串，否则要单独处理
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # 第一行
        for j in range(1, n2 + 1):
            # dp[0][j] = dp[0][j - 1] + 1
            dp[0][j] = j
        # 第一列
        for i in range(1, n1 + 1):
            # dp[i][0] = dp[i - 1][0] + 1
            dp[i][0] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        print(dp)
        return dp[n1][n2]

    def minDistance2(self, word1: str, word2: str) -> int:
        """状态转移方程2：优化一维数组+pre，dp[i] = min(dp[i-1], dp[i], pre) + 1
        """
        n1 = len(word1)
        n2 = len(word2)
        dp = [0] * (n2 + 1)

        # 第一行
        for i in range(1, n2 + 1): dp[i] = i

        for i in range(1, n1 + 1):
            # i-1,j-1
            temp = dp[0]
            # 第一列 i-1
            dp[0] = i
            for j in range(1, n2 + 1):
                # pre 来时刻保存 (i-1,j-1) 的值
                pre = temp
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j - 1], dp[j], pre) + 1
            print(dp)
        # print(dp)
        return dp[n2]

def main():
    param =  "horse"
    param2 = "ros"
    solution = Solution()
    ret = solution.minDistance(param, param2)
    print(ret)
    ret = solution.minDistance1(param, param2)
    print(ret)
    ret = solution.minDistance2(param, param2)
    print(ret)

'''72. 编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
