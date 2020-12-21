#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        什么时候使用 used 数组，什么时候使用 begin 变量
        有些朋友可能会疑惑什么时候使用 used 数组，什么时候使用 begin 变量。这里为大家简单总结一下：

        排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；
        组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），需要按照某种顺序搜索，此时使用 begin 变量。

        到底是i 还是i+1需要根据具体场景看包含当前元素不
        作者：liweiwei1419
        链接：https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
        """
        def backtrack(start, track):
            #结束条件:sum >= target
            if sum(track) == target: return res.append(track[:])
            if sum(track) > target: return

            for i in range(start, len(candidates)):
                #和上个数字相等就跳过
                if i > start and candidates[i] == candidates[i - 1]: continue
                # 做选择
                track.append(candidates[i])
                # 进入下一行决策：不包含当前元素
                backtrack(i + 1, track)
                # 撤销选择
                track.pop()

        res = []
        # candidates = list(set(candidates))
        candidates.sort()
        backtrack(0, [])
        return res


def main():
    param = [10,1,2,7,6,1,5]
    param2 = 8
    solution = Solution()
    ret = solution.combinationSum2(param, param2)
    print(ret)

'''40. 组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
