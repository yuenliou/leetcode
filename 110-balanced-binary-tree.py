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

'''110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true
 

提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
