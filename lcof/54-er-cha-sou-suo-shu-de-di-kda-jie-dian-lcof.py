#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode, build_binary_tree, level_order_travel, in_order_travel

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """中序遍历倒序的第 k 个节点"""
        def inOrderReverse(node):
            nonlocal k, result
            if node is None: return
            inOrderReverse(node.right)
            k -= 1
            if k == 0: result = node.val
            inOrderReverse(node.left)
        result = -1
        inOrderReverse(root)
        return result

def main():
    root = build_binary_tree([3,1,4,None,2])
    in_order_travel(root)
    solution = Solution()
    ret = solution.kthLargest(root, 1)
    print(ret)

'''剑指 Offer 54. 二叉搜索树的第k大节点

给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
