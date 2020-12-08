#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List, Callable

class MountainArray:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

def findInMountainArray(target: int, mountain_arr: 'MountainArray') -> int:
    def findPeakIndex(arr: MountainArray):
        """返回峰顶索引"""
        length = arr.length()
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr.get(mid) > arr.get(mid+1):
                right = mid
            else:
                left = mid + 1
        return left

    def findTargetIndex(arr: MountainArray, target: int, left: int, right: int, comp: Callable[[int, int], bool]):
        """二分求索引：数组升序&降序"""
        while left < right:
            mid = left + (right - left) // 2
            if comp(arr.get(mid), target):
                left = mid + 1
            else:
                right = mid
        return left if arr.get(left) == target else -1

    peakIndex = findPeakIndex(mountain_arr)
    if mountain_arr.get(peakIndex) == target: return peakIndex

    length = mountain_arr.length()
    left, right = 0, length - 1
    leftTargetIndex = findTargetIndex(mountain_arr, target, left, peakIndex, lambda x, y: x < y)
    if leftTargetIndex != -1: return leftTargetIndex
    rightTargetIndex = findTargetIndex(mountain_arr, target, peakIndex, right, lambda x, y: x > y)
    return rightTargetIndex

def main():
    param = [1,2,3,4,5,3,1,0]
    # param = [0,1,2,4,2,1]
    param = [1,5,2]
    mArr = MountainArray(param)
    ret = findInMountainArray(2, mArr)
    print(ret)

'''1095. 山脉数组中查找目标值

这是一个 交互式问题 ）

给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

如果不存在这样的下标 index，就请返回 -1。

 

何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

首先，A.length >= 3

其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
 

注意：

对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

 

示例 1：

输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
示例 2：

输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。
 

提示：

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-in-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
