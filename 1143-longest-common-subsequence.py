#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """带备忘录的递归算法：自顶向下"""
        def memoize(i, j):
            # 边界条件
            if i == -1: return 0
            if j == -1: return 0
            # 查缓存
            if cache[i][j] != 0:
                return cache[i][j]
            # 求解子问题
            if text1[i] == text2[j]:
                cache[i][j] = memoize(i - 1, j - 1) + 1
                return cache[i][j]
            else:
                cache[i][j] = max(memoize(i, j - 1), memoize(i - 1, j))
                return cache[i][j]

        n1, n2 = len(text1), len(text2)
        cache = [[0 for _ in range(n2)] for _ in range(n1)]
        ans = memoize(n1 - 1, n2 - 1)
        print(cache)
        return ans


    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        """状态转移方程：
        1.Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
        2.DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
        """
        n1 = len(text1)
        n2 = len(text2)
        # +1兼容空字符串，否则要单独处理
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        print(dp)
        return dp[n1][n2]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """状态转移方程2：优化一维数组+pre，dp[i] = max(dp[i-1], dp[i], pre) + 1"""
        n1 = len(text1)
        n2 = len(text2)
        dp = [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            # i-1,j-1
            pre = dp[0]
            dp[0] = 0
            for j in range(1, n2 + 1):
                # pre 来时刻保存 (i-1,j-1) 的值
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j - 1], dp[j])
                pre = temp
            print(dp)
        # print(dp)
        return dp[n2]

def main():
    param = "abcde"
    param2 = "ace"
    solution = Solution()
    ret = solution.longestCommonSubsequence(param, param2)
    print(ret)
    ret = solution.longestCommonSubsequence1(param, param2)
    print(ret)
    ret = solution.longestCommonSubsequence2(param, param2)
    print(ret)

'''1143. 最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

 

示例 1:

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
 

提示:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
