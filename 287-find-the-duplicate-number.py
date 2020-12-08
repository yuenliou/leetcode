#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def findDuplicate(nums: List[int]) -> int:
    """
    以 [2, 4, 5, 2, 3, 1, 6, 7] 为例，一共 8 个数，n + 1 = 8，n = 7，根据题目意思，每个数都在 1 和 7 之间。
    例如：区间 [1, 7][1,7] 的中位数是 4，遍历整个数组，统计小于等于 4 的整数的个数，如果不存在重复元素，最多为 4 个。
    等于 4 的时候区间 [1, 4][1,4] 内也可能有重复元素。但是，如果整个数组里小于等于 4 的整数的个数严格大于 4 的时候，就可以说明重复的数存在于区间 [1, 4][1,4]。
    说明：由于这个算法是空间敏感的，「用时间换空间」是反常规做法，算法的运行效率肯定不会高。
    链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
    """
    size = len(nums)
    left = 1
    right = size - 1

    while left < right:
        mid = left + (right - left) // 2

        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1
        # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
        # 此时重复元素一定出现在 [1, 4] 区间里

        if cnt > mid:
            # 重复的元素一定出现在 [left, mid] 区间里
            right = mid
        else:
            # if 分析正确了以后，else 搜索的区间就是 if 的反面
            # [mid + 1, right]
            left = mid + 1
    return left

def findDuplicate1(nums: List[int]) -> int:
    """
    [1,3,4,2,2] 数组下标 n 和数 nums[n] 建立一个映射关系 f(n)f(n)， 其映射关系 n->f(n) 为：
    0->1
    1->3
    2->4
    3->2
    4->2
    0->1->3->2->4->2->4->2->……
    https://leetcode-cn.com/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/
    """
    fast = slow = 0
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

def main():
    param = [1,3,4,2,2]
    # param = [3,1,3,4,2]
    ret = findDuplicate(param)
    print(ret)

'''287. 寻找重复数

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
