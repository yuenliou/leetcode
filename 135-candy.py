#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        左规则：当 ratings[i−1] < ratings[i] 时，i 号学生的糖果数量将比 i - 1 号孩子的糖果数量多。
        右规则：当 ratings[i] > ratings[i+1] 时，i 号学生的糖果数量将比 i + 1 号孩子的糖果数量多。
        对称遍历步骤：先给所有学生 1 颗糖。取以上 2 轮遍历 left 和 right 对应学生糖果数的 最大值 ，这样则 同时满足左规则和右规则 ，即得到每个同学的最少糖果数量
        """

        size = len(ratings)
        left = [1] * size
        right = [1] * size
        result = 0

        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(size - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(size):
            result += max(left[i], right[i])

        return result

    def candy1(self, ratings: List[int]) -> int:
        """
        优化循环次数：2层
        """
        size = len(ratings)
        left = [1] * size
        right = left[:]

        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        result = left[-1]
        for i in range(size - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            result += max(left[i], right[i])

        return result

    def candy2(self, ratings: List[int]) -> int:
        """
        优化循环次数：1层

        我们无需显式地额外分配糖果，只需要记录当前的递减序列长度，即可知道需要额外分配的糖果数量。
        同时注意当当前的递减序列长度和上一个递增序列等长时，需要把最近的递增序列的最后一个同学也并进递减序列中。

        链接：https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode-solution-f01p/
        """
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret

def main():
    param = [1, 3, 5, 3, 2, 1]
    solution = Solution()
    ret = solution.candy(param)
    print(ret)
    ret = solution.candy1(param)
    print(ret)
    ret = solution.candy2(param)
    print(ret)

'''135. 分发糖果

老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

 

示例 1：

输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2：

输入：[1,2,2]
输出：4
解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
