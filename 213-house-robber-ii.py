#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        """
        动态规划：分成两个198问题，只包含头和尾其中一个
        """
        size = len(nums)
        if size <= 0: return 0
        if size == 1: return nums[0]
        if size == 2: return max(nums[0], nums[1]) # 取其一

        def robs(start, end):#包含左右区间
            # 基本情况：
            pre0 = 0 # i-2
            pre = nums[start]# i-1
            curr = 0 # i

            for i in range(start + 2, end + 1):
                # 状态转移方程
                curr = max(pre, pre0 + nums[i - 1])
                pre0 = pre
                pre = curr
            return curr

        rob_head = robs(0, size - 1)
        rob_tail = robs(1, size)
        return max(rob_head, rob_tail)

def main():
    param = [1,2,3,1]
    param = [2,7,9,3,1]
    param = [2,1,1,2]
    param = [2,3,2]
    param = [1,1]
    solution = Solution()
    ret = solution.rob(param)
    print(ret)

'''213. 打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

 

示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [0]
输出：0
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
