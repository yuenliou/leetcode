#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
import heapq

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

def findKthLargest_v2(nums: List[int], k: int) -> int:
    """
    思路1：把 len 个元素都放入一个最小堆中，然后再 pop() 出 len - k 个元素，此时最小堆只剩下 k 个元素，堆顶元素就是数组中的第 k 个最大元素。
    思路2：把 len 个元素都放入一个最大堆中，然后再 pop() 出 k - 1 个元素，因为前 k - 1 大的元素都被弹出了，此时最大堆的堆顶元素就是数组中的第 k 个最大元素。
    优化思路：
    思路 3：只用 k 个容量的优先队列，而不用全部 len 个容量。
    思路 4：用 k + 1 个容量的优先队列，使得上面的过程更“连贯”一些，到了 k 个以后的元素，就进来一个，出去一个，让优先队列自己去维护大小关系。
    思路 5：综合考虑以上两种情况，总之都是为了节约空间复杂度。即 k 较小的时候使用最小堆，k 较大的时候使用最大堆。
    https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
    """
    heap = []
    # heapq.heapify(nums)
    for i in range(len(nums)): #思路1
        heapq.heappush(heap, nums[i])
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heap[0]

def findKthLargest_v3(nums: List[int], k: int) -> int:
    heap = []
    for i in range(k): #思路3
        heapq.heappush(heap, nums[i])

    for index in range(k, len(nums)):
        top = heap[0]
        if nums[index] > top:
            # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
            heapq.heapreplace(heap, nums[index])
    # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
    return heap[0]

def findKthLargest_v4(nums: List[int], k: int) -> int:
    length = len(nums)
    # list = heapq.nlargest(length, nums) #list[k-1]
    # list = heapq.nsmallest(length, nums) #list[length - k]
    list = heapq.nlargest(k, nums) #k在最后一位
    # list = heapq.nsmallest(length - k + 1, nums) #k在最后一位
    return list.pop()

def main():
    # param = [3,2,1,5,6,4] #5,k=2
    # param = [3,2,3,1,2,4,5,5,6] #4,k=4
    param = [3,7,5,2,1,8] #7,k=2
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
