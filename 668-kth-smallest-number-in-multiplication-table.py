#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.list_node import ListNode, MyListNode

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if k > m * n: return -1
        # enough(x) 描述了 x 是否足够大可以成为乘法表中的 k`th 值。
        def enough(x):
            count = 0
            for i in range(1, m + 1):
                # num这个值在当前第i行，有多少个值不比它大（<=num的个数）
                count += min(x // i, n)
            return count >= k

        def kthCount(x):
            count = 0
            row, col = 1, m
            while col > 0 and row <= n:
                # 行*列 <= mid的数量
                if col * row <= mid:
                    count += col
                    row += 1
                else:
                    col -= 1
            return count >= k

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            # 缩小左边界，查找右边界
            if not kthCount(mid): #[left mid]
                left = mid + 1
            else: #[mid + 1 right]
                right = mid

        return left

def main():
    m, n, k = 3, 3, 6

    solution = Solution()
    ret = solution.findKthNumber(m, n, k)
    print(ret)

'''668. 乘法表中第k小的数

几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：

输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
例 2：

输入: m = 2, n = 3, k = 6
输出: 6
解释: 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
注意：

m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
