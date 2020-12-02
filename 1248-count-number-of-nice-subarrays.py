#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    """前缀和+map"""
    length = len(nums)
    if length <= 0: return -1

    count = 0
    #枚举左右边界
    # for i in range(0, length):#left
    #     for j in range(i, length):#right
    #         sum = 0
    #         for n in range(i, j+1):#[left,right]
    #             # if nums[n] % 2: sum += 1
    #             sum += nums[n] % 2
    #         #求和之后对比
    #         if sum == k:
    #             count += 1

    #先固定左边界，然后枚举右边界
    for i in range(0, length):
        sum = 0
        for j in range(i, length):#gap++
            # print(i, j)
            sum += nums[j] % 2
            if sum == k:
                count += 1

    return count

def numberOfSubarrays1(nums: List[int], k: int) -> int:
    """前缀和+map"""
    length = len(nums)
    if length <= 0: return -1

    # map<前i个元素的前缀和(奇数数字的个数)，出现的次数> 默认值：特殊情况，和等于某个元素
    dict = {0:1}

    #前缀和
    pre = 0
    count = 0
    for i in range(0, length):
        pre += nums[i] % 2
        if pre - k in dict:
            count += dict[pre - k]
        dict[pre] = dict.get(pre, 0) + 1
    return count

def main():
    param = [1, 1, 2, 1, 1]
    # param = [2, 4, 6]
    # param = [2,2,2,1,2,2,1,2,2,2]
    ret = numberOfSubarrays1(param, 2)
    print(ret)

'''1248. 统计「优美子数组」

给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
