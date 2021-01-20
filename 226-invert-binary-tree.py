#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #递归交换左右节点
        if not root: return root
        root.left, root.right = root.right, root.left
        if root.left: self.invertTree(root.left)
        if root.right: self.invertTree(root.right)
        return root

def main():
    root = TreeNode(3)
    rLeft = TreeNode(4)
    rRight = TreeNode(5)

    root.setLeftNode(rLeft)
    root.setRightNode(rRight)

    rLeft.setLeftNode(TreeNode(1))
    rLeft.setRightNode(TreeNode(2))

    print('-root-')
    pre_order_travel(root)

    solution = Solution()
    ret = solution.invertTree(root)
    print('-pre-')
    pre_order_travel(ret)
    print('-in-')
    in_order_travel(ret)
    print('-post-')
    post_order_travel(ret)

'''226. 翻转二叉树

翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
