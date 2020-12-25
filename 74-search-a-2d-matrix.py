#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """标准二分查找：二维拉成一维"""
        def binary_search(left, right):
            while left <= right:
                #一维到二维：计算row&col
                pivot_idx = (left + right) // 2
                row = pivot_idx // n
                col = pivot_idx % n
                if matrix[row][col] < target:
                    left = pivot_idx + 1
                elif matrix[row][col] > target:
                    right = pivot_idx - 1
                else:
                    return True
            return False

        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        return binary_search(0, m * n - 1)

def main():
    param = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    param2 = 3
    solution = Solution()
    ret = solution.searchMatrix(param, param2)
    print(ret)

'''74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
输出：false
示例 3：

输入：matrix = [], target = 0
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
