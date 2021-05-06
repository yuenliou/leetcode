#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
import collections

class MonotonicQueue:
    """单调递减队列：push,pop,max都是O(1)"""
    def __init__(self):
        self.deque = collections.deque()

    def push(self, n):
        while self.deque and self.deque[-1] < n:
            self.deque.pop()
        self.deque.append(n)

    def pop(self, n):
        if self.deque and self.deque[0] == n:
            self.deque.popleft()

    def max(self):
        return self.deque[0]

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

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """滑动窗口之单调队列：https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/"""
        window = MonotonicQueue()
        res = []
        for i in range(len(nums)): # 形成窗口后
            if i < k - 1: #先填满窗口的前 k - 1
                window.push(nums[i])
            else: #窗口向前滑动
                window.push(nums[i])
                res.append(window.max())
                #滑动窗口移动时，左侧的最大元素不在范围内则移除
                window.pop(nums[i - k + 1])
        return res

def main():
    param = [1, 3, -1, -3, 5, 3, 6, 7]
    param2 = 3
    # param = [-7,-8,7,5,7,1,6,0]
    # param2 = 4
    solution = Solution()
    ret = solution.maxSlidingWindow(param, param2)
    print(ret)
    ret = solution.maxSlidingWindow1(param, param2)
    print(ret)
    ret = solution.maxSlidingWindow2(param, param2)
    print(ret)

'''剑指 Offer 59 - I. 滑动窗口的最大值

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
