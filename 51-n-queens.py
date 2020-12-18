#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        回溯算法详解框架：决策树：路径+选择(撤销)+结束
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484709&idx=1&sn=1c24a5c41a5a255000532e83f38f2ce4&chksm=9bd7fb2daca0723be888b30345e2c5e64649fc31a00b05c27a0843f349e2dd9363338d0dac61&scene=21#wechat_redirect
        经典的八皇后问题和N皇后问题
        https://mp.weixin.qq.com/s?__biz=MzU0ODMyNDk0Mw==&mid=2247487459&idx=1&sn=f45fc8231198edb3de2acc69e17986ea&chksm=fb419cc3cc3615d5d31d55072d5c2f58e4002aa8c1b637e889f1ef577e253943c04efc39c1b1d&token=1327182919&lang=zh_CN#rd
        """
        def isValid(board, row, col):
            """
            判断当前列有没有皇后, 因为他是一行一行往下走的，我们只需要检查走过的行数即可，
            通俗一点就是判断当前坐标位置的上面有没有皇后
            """

            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col] == 'Q': return False

            # 检查右上方是否有皇后互相冲突
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q': return False
                i, j = i - 1, j + 1

            # 检查左上方是否有皇后互相冲突
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q': return False
                i, j = i - 1, j - 1

            return True

        def deepcopy(board):
            ans = []
            for ele in board:
                ans.append(''.join(ele))
            return ans

        def backtrack(board, row):
            if row == n:
                # import copy
                # res.append(copy.deepcopy(board))
                res.append(deepcopy(board))
                return

            for col in range(n):
                # 排除不合法选择
                if not isValid(board, row, col): continue
                # 做选择
                board[row][col] = 'Q'
                # 进入下一行决策
                backtrack(board, row + 1)
                # 撤销选择
                board[row][col] = '.'

        # 字符串是常量不能直接赋值
        # board = [''.rjust(n, '.') for _ in range(n)]
        board = [['.'] * n for _ in range(n)]
        res = []
        backtrack(board, 0)
        return res

def main():
    param = 4
    solution = Solution()
    ret = solution.solveNQueens(param)
    print(ret)

'''51. N 皇后

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例：

输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 

提示：

皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
