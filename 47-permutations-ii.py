#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import itertools
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        回溯搜索 + 剪枝
        https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
        个人主页：https://liweiwei1419.gitee.io/leetcode-algo/
        语雀笔记：https://www.yuque.com/liweiwei1419/algo
        CSDN 博客：https://blog.csdn.net/lw_power
        """
        def dfs(depth, path):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                # 排序去重：not used[i - 1]保证每次都是拿从左往右第一个未被填过的数字
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                if used[i]: continue
                #状态变量
                used[i] = True
                #选择
                path.append(nums[i])
                #进入下一层决策树
                dfs(depth + 1, path)
                #状态重置
                used[i] = False
                #取消选择
                path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        #排序进行去重
        nums.sort()
        #利用py语言特性，减少参数传递 vs 46题
        dfs(0, [])
        return res

    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        def dfs(track):
            if len(track) == size:
                res.append(track[:])
                return

            for i in range(size):
                # 排序去重：not used[i - 1]保证每次都是拿从左往右第一个未被填过的数字
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                if used[i]: continue
                #状态变量
                used[i] = True
                #选择
                track.append(nums[i])
                #进入下一层决策树
                dfs(track)
                #状态重置
                used[i] = False
                #取消选择
                track.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        #排序进行去重
        nums.sort()
        #利用py语言特性，减少参数传递 vs 46题
        dfs([])
        return res

def main():
    param = [1, 2, 2]
    solution = Solution()
    ret = solution.permuteUnique(param)
    print(ret)
    param = [1, 2, 3]
    ret = solution.permuteUnique1(param)
    print(ret)

'''47. 全排列 II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
