#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        题解：https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/
        """
        def backtrack(start, path):
            #结束条件:无
            res.append(path[:])
            for i in range(start, len(nums)):
                #和上个数字相等就跳过
                if i > start and nums[i] == nums[i - 1]: continue
                # 做选择
                path.append(nums[i])
                # 进入下一行决策
                backtrack(i + 1, path)
                # 撤销选择
                path.pop()

        res = []
        nums.sort()
        backtrack( 0, [])
        return res

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        """数学归纳：https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485007&idx=1&sn=ceb42ba2f341af34953d158358c61f7c&chksm=9bd7f847aca071517fe0889d2679ead78b40caf6978ebc1d3d8355d6693acc7ec3aca60823f0&scene=21#wechat_redirect"""
        res = [[]]
        for i in nums:
            # print([[i] + j for j in res])
            res = res + [[i] + j for j in res]

        # return res

        ans = [[]]
        # 去重
        for num in res:
            if num not in ans:
                ans.append(num)
        return ans


def main():
    param = [1,2,2]
    solution = Solution()
    ret = solution.subsetsWithDup(param)
    print(ret)
    param = [1,2,3]
    ret = solution.subsetsWithDup2(param)
    print(ret)

'''90. 子集 II

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
