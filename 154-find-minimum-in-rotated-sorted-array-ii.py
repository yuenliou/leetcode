#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def minArray(numbers: List[int]) -> int:
    """https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/"""
    i, j = 0, len(numbers) - 1
    while i < j:
        m = (i + j) // 2
        if numbers[m] > numbers[j]: i = m + 1
        elif numbers[m] < numbers[j]: j = m
        else: j -= 1 # 最终的i不一定是旋转点
    return numbers[i]

def minArray2(numbers: List[int]) -> int:
    """剑指Offer??要崩溃了？？？"""
    def minInOrder(nums, start, end):
        res = nums[start]
        for i in range(start+1, end+1):
            if res > nums[i]:
                res = nums[i]
        return res

    head, tail = 0, len(numbers) - 1
    mid = head
    while numbers[head] >= numbers[tail]:
        if tail - head == 1: mid = tail; break
        mid = (head + tail) >> 1
        if numbers[head] == numbers[mid] and numbers[tail] == numbers[mid]:
            return minInOrder(numbers, head, tail)
        if numbers[head] <= numbers[mid]:
            head = mid
        elif numbers[tail] >= numbers[mid]:
            tail = mid
    return numbers[mid]

def minArray1(numbers: List[int]) -> int:
    head, tail = 0, len(numbers) - 1
    while head < tail:
        if numbers[head] >= numbers[tail]:
            head += 1
        else:
            tail -= 1
    return numbers[head]

def main():
    """
    思路1.划分两个已排序的数组O(n)
    思路2.二分法O(log2N)
    思路3.比较索引还是值？重复元素还是没有重复元素
    """
    param = [3, 4, 5, 1, 2]
    # param = [1, 2, 3, 4, 5]
    # param = [5, 4, 3, 2, 1]
    # param = [2, 2, 2, 2, 0, 1]
    # param = [2, 2, 2, 2, 2, 2]
    ret = minArray(param)
    print(ret)

'''154. 寻找旋转排序数组中的最小值 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
