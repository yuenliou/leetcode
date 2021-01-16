#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """
        限制：不能用除法，直接称复杂度太高，左右乘积数组循环次数：3层，2层，1层
        本质：本质就是两个dp数组，分别维护 i 左侧、右侧的乘积和。前缀积和后缀积
        """
        size = len(a)
        left = [1] * size
        right = [1] * size
        result = [1] * size

        for i in range(1, size):
            left[i] = left[i - 1] * a[i - 1]

        for i in range(size - 2, -1, -1):
            right[i] = right[i + 1] * a[i + 1]

        for i in range(size):
            result[i] = left[i] * right[i]

        return result

    def constructArr1(self, a: List[int]) -> List[int]:
        """
        优化循环次数：2层
        """
        size = len(a)
        left = [1] * size
        right = 1

        for i in range(1, size):
            left[i] = left[i - 1] * a[i - 1] #左边

        for i in range(size - 2, -1, -1):
            right *= a[i + 1] #右边
            left[i] *= right

        return left

    def constructArr2(self, a: List[int]) -> List[int]:
        """
        优化循环次数：1层，双端同时遍历
        """
        size = len(a)
        left = 1
        right = 1
        result = [1] * size

        for i in range(0, size):
            result[i] *= left
            # 持有左边的所有数的乘积
            left *= a[i]
            result[size - i - 1] *= right
            # 持有左边的所有数的乘积
            right *= a[size - i - 1]
        return result


def main():
    param = [1,2,3,4,5]
    solution = Solution()
    ret = solution.constructArr(param)
    print(ret)
    ret = solution.constructArr1(param)
    print(ret)
    ret = solution.constructArr2(param)
    print(ret)

'''剑指 Offer 66. 构建乘积数组

给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
注意：本题与主站 238 题相同：https://leetcode-cn.com/problems/product-of-array-except-self


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
