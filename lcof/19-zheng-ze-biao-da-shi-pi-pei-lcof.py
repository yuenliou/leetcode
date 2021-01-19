#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import functools

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 1.字符串为空，检测正则表达式
        if not s:
            # 如果正则串长度为奇数，必定不匹配，比如 "."、"ab*",必须是 a*b*这种形式，*在奇数位上
            if len(p) % 2: return False
            for i in range(1, len(p), 2):
                if p[i] != '*': return False
            return True

        # 2.字符串非空，正则表达式为空，return false
        if not p: return False

        # 3.c1 和 c2 分别是两个串的当前位，c3是正则串当前位的后一位，如果存在的话，就更新一下
        c1, c2 = s[0], p[0]
        c3 = p[1] if len(p) > 1 else ''

        # 4.和dp一样，后一位分为是 '*' 和不是 '*' 两种情况
        if c3 != '*':
            # 如果该位字符一样，或是正则串该位是 '.',也就是能匹配任意字符，就可以往后走
            if c1 == c2 or c2 == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            # 如果该位字符一样，或是正则串该位是 '.'，和dp一样，有看和不看两种情况
            if c1 == c2 or c2 == '.':
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                # 不一样，那么正则串这两位就废了，直接往后走
                return self.isMatch(s, p[2:])

    def isMatch1(self, s: str, p: str) -> bool:
        """https://leetcode-cn.com/problems/regular-expression-matching/solution/jian-ming-qing-xi-xie-fa-python3xiang-xi-zhu-shi-b/"""
        # 装饰符实现记忆化搜索，等价于Top-Down动态规划
        @functools.lru_cache(None)
        def recur(i,j):
            # 结束条件
            if j==len(p): return i==len(s)
            # 首字母匹配
            first_match = (len(s) > i) and (p[j] == s[i] or p[j] == '.')
            # 处理 `*`
            if len(p) >=j+2 and p[j+1] == '*':
                return recur(i, j+2) or (first_match and recur(i+1, j))
            # 处理首字母匹配
            return first_match and recur(i+1, j+1)
        return recur(0,0)

    def isMatch2(self, s: str, p: str) -> bool:
        """
        动态规划：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-s3jgn/

        状态定义： 设动态规划矩阵 dp ， dp[i][j] 代表字符串 s 的前 i 个字符和 p 的前 j 个字符能否匹配。
        转移方程： 需要注意，由于 dp[0][0] 代表的是空字符的状态， 因此 dp[i][j] 对应的添加字符是 s[i - 1] 和 p[j - 1] 。
        链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/jian-zhi-offer-19-zheng-ze-biao-da-shi-pi-pei-dong/

        1.如果 p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]；
        2.如果 p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1]；
        3.如果 p.charAt(j) == '*'：
        3.1如果 p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
        3.2如果 p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.'：
        dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a
        or dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
        or dp[i][j] = dp[i][j-2] // in this case, a* counts as empty

        作者：kao-la-7
        链接：https://leetcode-cn.com/problems/regular-expression-matching/solution/dong-tai-gui-hua-zen-yao-cong-0kai-shi-si-kao-da-b/
        """

        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                # *，区分看/不看两种情况
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    # 非*
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

    def isMatch3(self, s: str, p: str) -> bool:
        """动态规划:
        参考链接1：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/jian-zhi-offer-19-zheng-ze-biao-da-shi-pi-pei-dong/
        参考链接2：https://leetcode-cn.com/problems/regular-expression-matching/solution/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/
        """
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        # 两个空字符串能够匹配
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            # 首行 s 为空字符串，因此当 p 的偶数位为 * 时才能够匹配（即让 p 的奇数位出现 0 次，保持 p 是空字符串）。因此，循环遍历字符串 p ，步长为 2（即只看偶数位）。
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                # 非*，下一位
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == "*":
                        if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                            dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                        else:
                            dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]

def main():
    param = 'aa'
    param2 = 'a*'
    solution = Solution()
    ret = solution.isMatch(param, param2)
    print(ret)
    ret = solution.isMatch1(param, param2)
    print(ret)
    ret = solution.isMatch2(param, param2)
    print(ret)
    ret = solution.isMatch3(param, param2)
    print(ret)

'''剑指 Offer 19. 正则表达式匹配

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
