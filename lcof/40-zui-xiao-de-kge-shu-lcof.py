#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
import heapq
import random

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)

    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        """最小堆"""
        heap = arr[:]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap))
        return ans

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        """分区函数"""
        def partition(arr, pivot, left, right):
            """双指针分区"""
            i = left
            j = right
            pivotVal = arr[pivot]
            # 左右指针相遇的时候退出扫描循环
            while i < j:
                # 思考：为什么是右指针先扫而不是左指针先扫呢，大家自己想想吧哈哈，模拟一下就知道了
                while i < j and arr[j] >= pivotVal:
                    j -= 1  # 从右向左找第一个小于x的数
                while i < j and arr[i] <= pivotVal:
                    i += 1  # 从左向右找第一个大于x的数
                # 交换左右指针所停位置的数
                if i != j:
                    [arr[i], arr[j]] = [arr[j], arr[i]]
            # 最后交换基准数与指针相遇位置的数：只有先进行右指针的运动，才可以保证在相遇处的数字小于基准数
            [arr[pivot], arr[i]] = [arr[i], arr[pivot]]
            return i

        def randomPartition(arr, left, right):
            i = random.randint(left, right)
            arr[right], arr[i] = arr[i], arr[right]
            return partition(arr, left, left, right)

        def findKthBase(left, right) -> int:
            pivotIndex = randomPartition(arr, left, right)
            if pivotIndex > k:  # [0...p-1]
                return findKthBase(left, pivotIndex - 1)
            if pivotIndex < k:  # [p+1...n-1]
                return findKthBase(pivotIndex + 1, right)
            return pivotIndex

        if k >= len(arr): return arr
        return arr[:findKthBase(0, len(arr)-1)]

def main():
    param = [3,2,1]
    param2 = 2
    solution = Solution()
    ret = solution.getLeastNumbers(param, param2)
    print(ret)
    ret = solution.getLeastNumbers1(param, param2)
    print(ret)
    # param = [0, 0, 2, 3, 2, 1, 1, 2, 0, 4]
    # param2 = 10
    # param = [0,1,2,1]
    # param2 = 1
    ret = solution.getLeastNumbers2(param, param2)
    print(ret)

'''剑指 Offer 40. 最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
