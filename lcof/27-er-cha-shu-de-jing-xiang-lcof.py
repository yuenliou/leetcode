#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        #递归交换左右节点
        if not root: return root
        root.left, root.right = root.right, root.left
        if root.left: self.mirrorTree(root.left)
        if root.right: self.mirrorTree(root.right)
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
    ret = solution.mirrorTree(root)
    print('-pre-')
    pre_order_travel(ret)
    print('-in-')
    in_order_travel(ret)
    print('-post-')
    post_order_travel(ret)

'''剑指 Offer 27. 二叉树的镜像

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
