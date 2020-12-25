#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """对角线(二分)排除区域有重复：所以着手点是左下角/右上角，二分法也可以用递归划分四个矩阵"""
        def binary_search(matrix, target, start, vertical):
            lo = start
            hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

            while hi >= lo:
                mid = (lo + hi) // 2
                if vertical:  # searching a column
                    if matrix[start][mid] < target:
                        lo = mid + 1
                    elif matrix[start][mid] > target:
                        hi = mid - 1
                    else:
                        return True
                else:  # searching a row
                    if matrix[mid][start] < target:
                        lo = mid + 1
                    elif matrix[mid][start] > target:
                        hi = mid - 1
                    else:
                        return True

            return False

        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = binary_search(matrix, target, i, True)
            horizontal_found = binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """左下角开始：i-- 排除i行，j++排除j列"""
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        """右上角开始：i++ 排除i行，j--排除j列"""
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False

def main():
    param = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    param2 = 7
    solution = Solution()
    ret = solution.searchMatrix(param, param2)
    print(ret)
    ret = solution.searchMatrix1(param, param2)
    print(ret)
    ret = solution.searchMatrix2(param, param2)
    print(ret)

'''240. 搜索二维矩阵 II

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
 

示例 1：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
