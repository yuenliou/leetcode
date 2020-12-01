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
        else: j -= 1
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

'''153. 寻找旋转排序数组中的最小值

假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

 

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
示例 3：

输入：nums = [1]
输出：1
 

提示：

1 <= nums.length <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数都是 唯一 的
nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
