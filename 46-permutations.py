#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法与深度优先遍历：设计状态变量
        https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
        回溯算法详解框架：决策树：路径+选择(撤销)+结束
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484709&idx=1&sn=1c24a5c41a5a255000532e83f38f2ce4&chksm=9bd7fb2daca0723be888b30345e2c5e64649fc31a00b05c27a0843f349e2dd9363338d0dac61&scene=21#wechat_redirect
        """
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                #res.append(path) #拷贝
                res.append(path[:])
                # res.append(path.copy())
                return

            for i in range(size):
                if not used[i]:
                    #状态变量
                    used[i] = True
                    #选择
                    path.append(nums[i])
                    #进入下一层决策树
                    dfs(nums, size, depth + 1, path, used, res)
                    #状态重置
                    used[i] = False
                    #取消选择
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        """https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/"""
        return list(itertools.permutations(nums))

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """通过数组元素减少变相控制状态"""
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res

    def permute3(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, state, res):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                # print(i, state, state >> i, (state >> i) & 1, 1 << i, state ^ (1 << i))

                if ((state >> i) & 1) == 0:
                    # print(state, i)
                    dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)

        size = len(nums)
        if size == 0:
            return []

        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)
        return res

def main():
    param = [1, 2, 3]
    solution = Solution()
    ret = solution.permute(param)
    print(ret)
    ret = solution.permute1(param)
    print(ret)
    ret = solution.permute2(param)
    print(ret)
    ret = solution.permute3(param)
    print(ret)

'''46. 全排列

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
