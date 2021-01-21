#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, build_binary_tree

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """dfs"""
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum1(self, root: TreeNode, targetSum: int) -> bool:
        """回溯"""
        def preOrder(node, path):
            if not node: return False
            #状态
            path.append(node.val) # 先序
            if sum(path) == targetSum and not node.left and not node.right:
                return True
            left = preOrder(node.left, path[:])
            right = preOrder(node.right, path[:])
            #恢复&上面新建数组不用pop
            # path.pop()
            return left or right

        return preOrder(root, [])

def main():
    root = build_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    solution = Solution()
    ret = solution.hasPathSum(root, 22)
    print(ret)
    ret = solution.hasPathSum1(root, 22)
    print(ret)

'''112. 路径总和

给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：false
示例 3：

输入：root = [1,2], targetSum = 0
输出：false
 

提示：

树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
