#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """维护单调递减队列：窗口滑动添加了元素 nums[j + 1] ，需将 deque 内所有 < nums[j + 1] 的元素删除"""
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        # 记录结果
        res = [deque[0]]
        for i in range(k, len(nums)): # 形成窗口后
            # i-k是已经在区间外了，如果首位等于nums[i-k]，那么说明此时首位值已经不再区间内了，需要删除
            if deque[0] == nums[i - k]: # case [1,-1]，1
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """单调队列经典题目：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-i-hua-dong-chuang-kou-de-zui-da-1-6/"""
        deque = collections.deque()
        res, n = [], len(nums)
        #Python 通过 zip(range(), range()) 可实现滑动窗口的左右边界 i, j 同时遍历。
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft() # 删除 deque 中对应的 nums[i-1]
            while deque and deque[-1] < nums[j]:
                deque.pop() # 保持 deque 递减
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0]) # 记录窗口最大值
        return res

def main():
    param = [1,3,-1,-3,5,3,6,7]
    param2 = 3
    solution = Solution()
    ret = solution.maxSlidingWindow(param, param2)
    print(ret)
    ret = solution.maxSlidingWindow1(param, param2)
    print(ret)

'''239. 滑动窗口最大值

给你一个zheng's数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
示例 4：

输入：nums = [9,11], k = 2
输出：[11]
示例 5：

输入：nums = [4,-2], k = 2
输出：[4]
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
