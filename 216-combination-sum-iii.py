#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """k 限制了树的高度，n 限制了树的宽度。"""
        def backtrack(start, track):
            #结束条件:到大树的底部
            if sum(track) == n and len(track) == k: return res.append(track[:])
            if sum(track) > n or len(track) > k: return

            for i in range(start, 10):
                # 做选择
                track.append(i)
                # 进入下一行决策
                backtrack(i + 1, track)
                # 撤销选择
                track.pop()

        res = []
        if n <= 0 or k <= 0: return []
        backtrack(1, [])
        return res

    def combinationSum3_1(self, k: int, n: int) -> List[List[int]]:
        """k 限制了树的高度，n 限制了树的宽度。"""
        def backtrack(start, track):
            #结束条件:到大树的底部
            if sum(track) == n and len(track) == k: return res.append(track[:])
            #剪枝 (n - start + 1) < k
            if sum(track) > n or len(track) > k or len(track) + (n - start + 1) < k: return

            # 考虑选择当前位置
            track.append(start)
            backtrack(start + 1, track)
            track.pop()
            # 考虑不选择当前位置
            backtrack(start + 1, track)

        res = []
        if n <= 0 or k <= 0: return []
        backtrack(1, [])
        return res


def main():
    param = 3
    param2 = 7
    solution = Solution()
    ret = solution.combinationSum3(param, param2)
    print(ret)
    ret = solution.combinationSum3_1(param, param2)
    print(ret)

'''216. 组合总和 III

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
