#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, build_binary_tree

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
    root = build_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])

    solution = Solution()
    ret = solution.pathSum(root, 22)
    print(ret)

'''113. 路径总和 II

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

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


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
