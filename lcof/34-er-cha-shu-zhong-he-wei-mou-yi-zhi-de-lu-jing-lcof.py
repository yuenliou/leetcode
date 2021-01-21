#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, build_binary_tree, level_order_travel

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """dfs+先序"""
        def preOrder(node, path):
            if not node: return
            #状态
            path.append(node.val) # 先序
            if sum(path) == targetSum and not node.left and not node.right:
                #不能return
                result.append(path[:])
            preOrder(node.left, path)
            preOrder(node.right, path)
            #恢复
            path.pop()

        result = []
        preOrder(root, [])
        return result

    def pathSum1(self, root: TreeNode, sum: int) -> List[List[int]]:
        """先序遍历 + 路径记录 + tar-- """
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res


def main():

    root = build_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print('-level-')
    level_order_travel(root)

    solution = Solution()
    ret = solution.pathSum(root, 22)
    print(ret)

'''剑指 Offer 34. 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000
注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
