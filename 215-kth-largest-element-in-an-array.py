#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    def partition(arr, left, right):
        """经典分区：遍历数组元素，将小于 pivot 的元素放到左边，将大于 pivot 的元素放到右边"""
        pivot = right  # 右边为分区点
        j = left
        for i in range(left, right):
            if arr[i] < arr[pivot]:  # >降序
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        # 最后交换基准数与指针停留位置(piovt在右边不用-1)
        arr[pivot], arr[j] = arr[j], arr[pivot]
        return j

    target = len(nums) - k
    def findKthBase(left, right) -> int:
        pivotIndex = partition(nums, left, right)
        if pivotIndex > target: #[0...p-1]
            return findKthBase(left, pivotIndex-1)
        if pivotIndex < target: #[p+1...n-1]
            return findKthBase(pivotIndex+1, right)
        return nums[pivotIndex]

    def findKthBase_iter(left, right) -> int:
        while True:
            pivotIndex = partition(nums, left, right)
            if pivotIndex > target: #[0...p-1]
                right = pivotIndex - 1
            elif pivotIndex < target: #[p+1...n-1]
                left = pivotIndex + 1
            else:
                return nums[pivotIndex]

    return findKthBase(0, len(nums)-1)

def main():
    # param = [3,2,1,5,6,4]
    # param = [3,2,3,1,2,4,5,5,6]
    param = [3,7,5,2,1,8] #7
    ret = findKthLargest(param, 2)
    print(ret)

'''215. 数组中的第K个最大元素

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
