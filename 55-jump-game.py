#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """贪心策略：如果一个位置能够到达，那么这个位置左侧所有位置都能到达。"""
        farthest = 0
        for i in range(len(nums)):
            # print(i, farthest)
            if i > farthest: return False
            farthest = max(farthest, i + nums[i])
        return True

    def canJump2(self, nums: List[int]) -> bool:
        """贪心策略2：向前遍历记录可以到达终点的最前的位置。"""
        start = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            print(i, start)
            if i + nums[i] >= start:
                start = i
        return 0 == start

def main():
    param = [2,3,1,1,4]
    # param = [3,2,1,0,4]
    solution = Solution()
    ret = solution.canJump(param)
    print(ret)
    ret = solution.canJump2(param)
    print(ret)

'''55. 跳跃游戏

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
