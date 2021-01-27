#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, build_binary_tree, level_order_travel, in_order_travel

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """迭代"""
        if p.val > q.val: p, q = q, p  # 保证 p.val < q.val
        while root:
            if root.val < p.val:  # p,q 都在 root 的右子树中
                root = root.right  # 遍历至右子节点
            elif root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left  # 遍历至左子节点
            else:
                break
        return root

def main():
    root = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(8)
    root.setLeftNode(n2)
    root.setRightNode(n3)

    n4 = TreeNode(0)
    n5 = TreeNode(4)
    n2.setLeftNode(n4)
    n2.setRightNode(n5)

    n6 = TreeNode(7)
    n7 = TreeNode(9)
    n3.setLeftNode(n6)
    n3.setRightNode(n7)

    solution = Solution()
    ret = solution.lowestCommonAncestor(root, n2, n3)
    print(ret.val)

'''235. 二叉搜索树的最近公共祖先

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
