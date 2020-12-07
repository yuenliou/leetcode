#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def search(nums: List[int], target: int) -> bool:
    """
    思路：根据中间数和任意边界的大小确定有序区间
    理解：中间元素把待搜索区间分成了两部分，两部分具有的性质是至少有一部分是有序的。
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/
    """
    length = len(nums)

    # if length == 0: return -1
    if length == 0: return False

    left, right = 0, length - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # return mid
            return True

        #中间元素和右边界比较，使用右中位数
        if nums[mid] < nums[right]:
            #右边有序
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] > nums[right]:
            #左边有序
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            #确定不了到底是前面有序还是后面有序，right--去掉一个干扰项
            right -= 1

    #后处理
    # return left if nums[left] == target else -1
    return True if nums[left] == target else False


def main():
    param = [4,5,6,7,0,1,2]
    # param = [4,5,6,7]
    # param = [1,1,1,2,1,1]
    # param = [3,1,1,1]
    ret = search(param, 8)
    print(ret)

'''81. 搜索旋转排序数组 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
