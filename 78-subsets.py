#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        题解：https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/
        """
        def backtrack(nums, size, start, path):
            #结束条件:无
            res.append(path[:])
            for i in range(start, size):
                # 做选择
                path.append(nums[i])
                # 进入下一行决策
                backtrack(nums, size, i + 1, path)
                # 撤销选择
                path.pop()

        res = []
        size = len(nums)
        backtrack(nums, size, 0, [])
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        数学归纳递归：subset([1,2,3]) = A + [A[i].add(3) for i = 1..len(A)]
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485007&idx=1&sn=ceb42ba2f341af34953d158358c61f7c&chksm=9bd7f847aca071517fe0889d2679ead78b40caf6978ebc1d3d8355d6693acc7ec3aca60823f0&scene=21#wechat_redirect
        """
        if len(nums) == 0: return [[]]
        last = nums.pop()
        res = self.subsets1(nums)

        size = len(res)
        for i in range(size):
            #深copy
            res.append(res[i][:])
            res[len(res)-1].append(last)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """数学归纳迭代"""
        res = [[]]
        for i in nums:
            # print([[i] + j for j in res])
            res = res + [[i] + j for j in res]
        return res

        # 去重
        # ans = [[]]
        # for num in res:
        #     if num not in ans:
        #         ans.append(num)
        # return ans

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        """二进制计数： """
        res = []
        # 2 ** len = 8
        n =  1 << len(nums)
        for i in range(n):
            path = []
            # print(i, res)
            for j in range(n):
                # mask & (1 << i)
                if i & 1 << j:
                    path.append(nums[j])

                # if i & 1 == 1:
                #     path.append(nums[j])
                # i = i >> 1

            res.append(path)
        return res

    def subsets4(self, nums: List[int]) -> List[List[int]]:
        """二进制递归枚举：https://leetcode-cn.com/problems/subsets/solution/er-jin-zhi-wei-zhu-ge-mei-ju-dfssan-chong-si-lu-9c/ """
        def backtrack(cur, path):
            # 终止返回结果
            if cur == len(nums): return res.append(path[:])
            # 考虑选择当前位置
            path.append(nums[cur])
            backtrack(cur + 1, path)
            path.pop()
            # 考虑不选择当前位置
            backtrack(cur + 1, path)
        res = []
        backtrack(0, [])
        return res

def main():
    param = [1,2,3]
    solution = Solution()
    ret = solution.subsets(param)
    print(ret)
    ret = solution.subsets1(param)
    print(ret)
    param = [1,2,3] #subsets1会改变param
    ret = solution.subsets2(param)
    print(ret)
    ret = solution.subsets3(param)
    print(ret)
    ret = solution.subsets4(param)
    print(ret)

'''78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
