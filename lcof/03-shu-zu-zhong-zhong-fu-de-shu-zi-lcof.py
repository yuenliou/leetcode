#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def findRepeatNumber(nums: List[int]) -> int:
    length = len(nums)
    for i in range(length):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            #这个地方不能用快捷写法
            # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            temp = nums[i]
            nums[i] = nums[temp]
            nums[temp] = temp
    return -1

def findRepeatNumber1(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

def main():
    """
    思路1.字典或者集合记录已遍历过的num
    思路2.先排序然后看是否有相邻的重复元素
    思路3.数组下标和元素的值一一对应，有点类似计数排序
    """
    param = [2, 3, 1, 0, 2, 5, 3]
    ret = findRepeatNumber(param)
    print(ret)

'''剑指 Offer 03. 数组中重复的数字

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：

2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
