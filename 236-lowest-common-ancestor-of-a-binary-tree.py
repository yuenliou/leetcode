#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, build_binary_tree, level_order_travel, in_order_travel

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """后续遍历"""
        # 如果 p和q中有等于 root的，那么它们的最近公共祖先即为root（一个节点也可以是它自己的祖先）
        if not root or root == p or root == q: return root
        # 递归遍历左子树，只要在左子树中找到了p或q，则先找到谁就返回谁
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归遍历右子树，只要在右子树中找到了p或q，则先找到谁就返回谁
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return None  # 1. 没有公共祖先
        if not left: return right  # 3.如果在左子树中 p和 q都找不到，则 p和 q一定都在右子树中，右子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        if not right: return left  # 4.否则，如果 left不为空，在左子树中有找到节点（p或q），这时候要再判断一下右子树中的情况，如果在右子树中，p和q都找不到，则 p和q一定都在左子树中，左子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        return root  # 2. if left and right: 否则，当 left和 right均不为空时，说明 p、q节点分别在 root异侧, 最近公共祖先即为 root

def main():
    root = TreeNode(3)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    root.setLeftNode(n2)
    root.setRightNode(n3)

    n4 = TreeNode(6)
    n5 = TreeNode(2)
    n2.setLeftNode(n4)
    n2.setRightNode(n5)

    n6 = TreeNode(0)
    n7 = TreeNode(8)
    n3.setLeftNode(n6)
    n3.setRightNode(n7)

    solution = Solution()
    ret = solution.lowestCommonAncestor(root, n2, n3)
    print(ret.val)

'''236. 二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
