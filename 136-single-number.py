#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from functools import reduce

def singleNumber(nums: List[int]) -> int:
    """
    思路：排序，哈希，位运算(异或) 0^1 = 1, 1^1 = 0
    """

    # n = 0
    # for val in nums:
    #     n ^=  val
    # return n

    return reduce(lambda x, y: x ^ y, nums)


def main():
    # param = [2,2,1]
    param = [4,1,2,1,2]
    ret = singleNumber(param)
    print(ret)

'''136. 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
