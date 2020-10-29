#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    rst = []
    n = len(nums)
    # 索引号之排序
    for i in range(n):
        print('times', i)
        # [4,3,2,7,8,2,3,1]
        while nums[nums[i] - 1] != nums[i]:
            # 交换之temp
            num_i = nums[i] - 1
            nums[num_i], nums[i] = nums[i], nums[num_i]
            print(nums)
    # print(nums) # [1, 2, 3, 4, 3, 2, 7, 8]
    for i in range(n):
        if i != nums[i] - 1:
            rst.append(nums[i])
    # for idx, val in enumerate(nums, 1):
    #     if val != idx:
    #         rst.append(val)

    return rst

def findDuplicates_abs(nums: List[int]) -> List[int]:
    """取相反数标记已经访问过该位置"""
    ret = list()
    # 索引号之绝对值
    for num in nums:
        i = abs(num) - 1
        if nums[i] < 0:
            ret.append(abs(num))
            # print(ret)
        nums[i] = -nums[i]
        # print(nums)
    return ret

def findDuplicates_sort(nums: List[int]) -> List[int]:
    nums.sort()
    retSet = set()
    for i, num in enumerate(nums[:-1]):
        if num == nums[i+1]:
            retSet.add(num)
    return list(retSet)

def findDuplicates_hash(nums: List[int]) -> List[int]:
    hashSet = set()
    retSet = set() #集合不重复
    for num in nums:
        if num in hashSet:
            retSet.add(num)
        hashSet.add(num)
    return list(retSet)

def main():
    param = [4,3,2,7,8,2,3,1]
    ret = findDuplicates(param)
    print(ret)

'''442. 数组中重复的数据

给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
