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

'''剑指 Offer 11. 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
