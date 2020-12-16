#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        贪心策略2：记录位置i步长范围内哪个位置能到达的距离最远，此步就走哪个位置。
        参考：https://segmentfault.com/a/1190000023758133
        """
        aim, farthest, ans = 0, 0, 0
        for i in range(len(nums) - 1):
            #找能跳的最远的
            aim = max(aim, i + nums[i])
            # print(i, farthest, aim)
            #遇到边界，就更新边界，并且步数加一
            if i == farthest:
                ans += 1
                farthest = aim
        return ans

    def jump1(self, nums: List[int]) -> int:
        """
        贪心策略：别想那么多，就挨着跳吧 II。模拟过程
        参考：https://leetcode-cn.com/problems/jump-game-ii/solution/45-by-ikaruga/
        """
        ans, start, end = 0, 0, 1
        while end < len(nums):
            maxPos = 0
            for i in range(start, end):
                #找能跳的最远的
                maxPos = max(maxPos, i + nums[i])
            start = end # 下一次起跳点范围开始的格子
            end = maxPos + 1 # 下一次起跳点范围结束的格子
            ans += 1 # 跳跃次数
        return ans

    def jump2(self, nums: List[int]) -> int:
        """
        贪心策略1：每一次记录能到终点的最前的位置，并更新终点位置。
        解法二：顺瓜摸藤：https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/
        """
        aim = len(nums) - 1
        cnt = 0
        while aim:
            for i in range(len(nums)):
                if i + nums[i] >= aim:
                    aim = i
                    cnt += 1
                    break
        return cnt

def main():
    param = [2,3,1,1,4]
    # param = [3,2,1,0,4]
    solution = Solution()
    ret = solution.jump(param)
    print(ret)
    ret = solution.jump1(param)
    print(ret)
    ret = solution.jump2(param)
    print(ret)

'''45. 跳跃游戏 II

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
