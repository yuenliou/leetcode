#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #前序遍历和对称前序遍历相同
        def symmetry(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            #root相等
            if root1.val != root2.val: return False
            #左右子树相等
            return symmetry(root1.left, root2.right) and symmetry(root1.right, root2.left)
        return symmetry(root, root)

def main():
    root = TreeNode(3)
    rLeft = TreeNode(4)
    rRight = TreeNode(5)

    root.setLeftNode(rLeft)
    root.setRightNode(rRight)

    rLeft.setLeftNode(TreeNode(1))
    rLeft.setRightNode(TreeNode(2))

    solution = Solution()
    ret = solution.isSymmetric(root)
    print(ret)

'''剑指 Offer 28. 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
