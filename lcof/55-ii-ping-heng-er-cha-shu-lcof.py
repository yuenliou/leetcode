#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, build_binary_tree, level_order_travel, in_order_travel

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        漫谈递归：递归的思想 http://www.nowamagic.net/librarys/veda/detail/2314
        第一个算法还是比较好理解的，但第二个就不那么好理解了。
        第一个算法的思想是：如果这个树是空，则返回0；否则先求左边树的深度，再求右边数的深度，然后对这两个值进行比较哪个大就取哪个值+1。
        而第二个算法，首先应该明白isB函数的功能，它对于空树返回0，对于平衡树返回树的深度，对于不平衡树返回-1。明白了函数的功能再看代码就明白多了，只要有一个函数返回了-1，则整个函数就会返回-1。（具体过程只要认真看下就明白了）
        """
        def isB(root):
            #附带剪枝，任意树返回-1即不平衡
            if not root: return 0
            left = isB(root.left)
            if left == -1: return -1
            right = isB(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return isB(root) != -1

def main():
    root = build_binary_tree([3,9,20,None,None,15,7])
    solution = Solution()
    ret = solution.isBalanced(root)
    print(ret)

'''剑指 Offer 55 - II. 平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

限制：

1 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
