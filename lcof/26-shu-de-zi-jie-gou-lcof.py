#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        #t1是否有t2
        def doseTree1HasTree2(t1, t2):
            if not t2: return True
            if not t1: return False
            if t1.val != t2.val: return False
            #左右节点都相等
            return doseTree1HasTree2(t1.left, t2.left) and doseTree1HasTree2(t1.right, t2.right)

        result = False
        if A and B:
            if A.val == B.val:
                result = doseTree1HasTree2(A, B)
            if not result:
                # 左子树是否有B
                result = self.isSubStructure(A.left, B)
            if not result:
                # 右子树是否有B
                result = self.isSubStructure(A.right, B)
        return result

def main():
    root = TreeNode(3)
    rLeft = TreeNode(4)
    rRight = TreeNode(5)

    root.setLeftNode(rLeft)
    root.setRightNode(rRight)

    rLeft.setLeftNode(TreeNode(1))
    rLeft.setRightNode(TreeNode(2))

    root2 = TreeNode(4)
    root2.setLeftNode(TreeNode(1))

    solution = Solution()
    ret = solution.isSubStructure(root, root2)
    print(ret)

'''剑指 Offer 26. 树的子结构

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
