#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    """枚举"""
    length = len(nums)
    if length <= 0: return []

    count = [0] * length

    for i in range(0, length):
        for j in range(0, length):
            if i != j and nums[j] < nums[i]:
                count[i] += 1
    return count

def smallerNumbersThanCurrent0(nums: List[int]) -> List[int]:
    """
    排序与映射：排序之后，其实每一个数值的下标就代表这前面有几个比它小的了。
    https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/solution/1365-you-duo-shao-xiao-yu-dang-qian-shu-zi-de-s-35/    """
    length = len(nums)
    if length <= 0: return []

    #排序
    nums2 = sorted(nums)

    #逆序哈希(相同元素取最左面的数值和下标)
    map = {}
    for i in range(length - 1, -1, -1):
        map[nums2[i]] = i

    count = [0] * length
    for i in range(length):
        count[i] = map[nums[i]]

    return count

def smallerNumbersThanCurrent01(nums: List[int]) -> List[int]:
    """
    快速排序:官方，索引下标就是目标答案的个数，关键维护好索引与数组的关系
    我们也可以将数组排序，并记录每一个数在原数组中的位置。对于排序后的数组中的每一个数，我们找出其左侧第一个小于它的数，这样就能够知道数组中小于该数的数量。
    https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/solution/you-duo-shao-xiao-yu-dang-qian-shu-zi-de-shu-zi--2/
    """
    length = len(nums)
    if length <= 0: return []

    # data = [[0] * 2] * 5 # array是同一个引用
    # data = [[0 for i in range(2)] for j in range(5)]
    data = [[0, 0] for _ in range(length)]

    #下面会对二维数组排序
    for i in range(length):
        data[i][0] = nums[i]
        data[i][1] = i
    #print(data)

    # data.sort() 等价下面写法
    data.sort(key=lambda x:x[0], reverse=False)
    #print(data)

    prev = -1
    count = [0] * length
    for i in range(length):
        if prev == -1 or data[i][0] != data[i - 1][0]:
            prev = i
        count[data[i][1]] = prev
    return count

def smallerNumbersThanCurrent1(nums: List[int]) -> List[int]:
    """
    排序与映射：你的索引是多少，就有多少个数字小于你[严格说应该是 小于等于你]
    https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/solution/java-pai-xu-yu-ying-she-by-lzhlyle/385413/
    """
    length = len(nums)
    if length <= 0: return []

    map = {}# int -> set
    for i, n in enumerate(nums):
        if n not in map:
            map[n] = set()
        map[n].add(i)

    nums2 = sorted(nums)

    count = [0] * length
    for i in range(length-1, -1, -1):
        # 倒序，方便处理同值的情况,此行为补充优化：前面还有同值的，那就跳过这次，等下次再一并赋值
        if i - 1 >= 0 and nums2[i] == nums2[i - 1]: continue
        # 同值的所有索引都更新
        for j in map[nums2[i]]: count[j] = i
    return count

def smallerNumbersThanCurrent2(nums: List[int]) -> List[int]:
    """
    计数排序
    https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/solution/java-pai-xu-yu-ying-she-by-lzhlyle/385413/
    """
    length = len(nums)
    if length <= 0: return []

    #提示：0 <= nums[i] <= 100

    freq = [0] * 101
    #统计出现频率 frequency 索引即数值
    for n in nums: freq[n] += 1
    #对频率(而非对原数组nums)从前到后累加
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]

    count = [0] * length
    for i in range(length):
        if nums[i] > 0:
            #比i小的数目 刚好 等于频次计数数组的value
            count[i] = freq[nums[i] - 1]
    # print(freq)
    # [0, 1, 3, 4, 4, 4, 4, 4, 5, 5...
    # i = 0, num[i] = 8, count[0] = freq[7]
    return count

def main():
    param = [8,1,2,2,3]
    # param = [6,5,4,8]
    # param = [7,6,7,7]
    ret = smallerNumbersThanCurrent01(param)
    print(ret)

'''1365. 有多少小于当前数字的数字

给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。

 

示例 1：

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
示例 2：

输入：nums = [6,5,4,8]
输出：[2,1,0,3]
示例 3：

输入：nums = [7,7,7,7]
输出：[0,0,0,0]
 

提示：

2 <= nums.length <= 500
0 <= nums[i] <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
