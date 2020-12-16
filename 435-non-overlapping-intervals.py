#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """贪心思路: 1. 排序找出第一个区间end记为x, 2.把所有与x相交的区间干掉, 3.重复1.2"""
        length = len(intervals)
        if length <= 0: return 0

        #按照end升序排列
        intervals.sort(key=lambda e: e[1])
        print(intervals)

        #不重叠区间个数，至少有一个(第一个)
        cnt = 1
        x_end = intervals[0][1]

        for intvs in intervals:
            start = intvs[0]
            if start >= x_end:
                cnt += 1
                x_end = intvs[1]
        # 重叠需要删去的个数
        return length - cnt

def main():
    param = [ [1,2], [2,3], [3,4], [1,3], [3, 4] ]
    # param = [ [1,2], [1,2], [1,2] ]
    solution = Solution()
    ret = solution.eraseOverlapIntervals(param)
    print(ret)

'''435. 无重叠区间

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
