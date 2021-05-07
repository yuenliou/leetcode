#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        思路1：暴力解
        思路2：单调栈：主动查找O`2，被动查找单调栈。是因为每次找下一个最大值，栈内存放的永远是还没更新答案的下标
        类似题目：[1118.一月有多少天:索引间隔]：https://leetcode-cn.com/problems/number-of-days-in-a-month/
        """
        n = len(nums)
        # 初始化-1
        res = [-1] * n
        # 栈存放的是下标
        stack = []
        # 拼接一个数组达到循环数组的目的
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res

def main():
    param = [1,2,1]
    solution = Solution()
    ret = solution.nextGreaterElements(param)
    print(ret)


'''503. 下一个更大元素 II

给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
