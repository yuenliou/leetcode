#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        思路：dfs回溯，超时
        """
        def dfs(path):
            #边界条件：最后处理超时
            if len(path) == len(s):
                res = ''.join(path)
                if res not in ans:
                    ans.append(res)
                return

            for j in range(len(s)):
                if visited[j]: continue

                # 状态标记
                visited[j] = 1
                path.append(s[j])

                dfs(path)

                # 状态恢复
                visited[j] = 0
                path.pop()

        #答案数组
        ans = []
        #状态数组
        visited = [0] * len(s)
        #遍历字符串
        dfs([])
        return ans

    def permutation1(self, s: str) -> List[str]:
        """
        思路：dfs回溯，剪枝：1，排序去重i vs i-1，2，每位对应一个set
        """
        def dfs(depth, path):
            #边界条件：
            if len(path) == len(s): return ans.append(''.join(path))

            for j in range(len(s)):
                # 排序去重：not used[i - 1]保证每次都是拿从左往右第一个未被填过的数字
                if j > 0 and s[j] == s[j - 1] and not visited[j - 1]: continue

                if visited[j]: continue

                # 状态标记
                visited[j] = 1
                path.append(s[j])

                dfs(depth+1, path)

                # 状态恢复
                visited[j] = 0
                path.pop()

        #答案数组
        ans = []
        #状态数组
        visited = [0] * len(s)
        #排序
        s = "".join((lambda x: (x.sort(), x)[1])(list(s)))
        # s = "".join(sorted(s, key=str.lower))
        #遍历字符串
        dfs(0, [])
        return ans

def main():
    param = 'aac'
    solution = Solution()
    ret = solution.permutation(param)
    print(ret)
    ret = solution.permutation1(param)
    print(ret)

'''剑指 Offer 38. 字符串的排列

输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8
注意：本题与主站 47 题相同：https://leetcode-cn.com/problems/permutations-ii


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
