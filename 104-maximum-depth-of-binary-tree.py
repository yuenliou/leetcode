#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from collections import deque
from datatype.tree_node import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """dfs"""
        if not root:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            # return l + 1 if l > r else r + 1
            return max(l, r) + 1

    def maxDepth2(self, root: TreeNode) -> int:
        """bfs"""
        if not root: return 0
        cnt = 0
        queue = deque()
        queue.append(root)
        while len(queue):  # isEmpty()
            temp = []
            # cnt = len(queue); while cnt: ...; cnt -= 1
            for _ in range(len(queue)):
                root = queue.pop()  # list.pop(0)
                temp.append(root.val)
                if root.left:
                    queue.appendleft(root.left)
                if root.right:
                    queue.appendleft(root.right)
            cnt += 1
        return cnt

def main():
    root = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    root.setLeftNode(n2)
    root.setRightNode(n3)
    n3.setLeftNode(n4)
    n3.setRightNode(n5)

    solution = Solution()
    ret = solution.maxDepth2(root)
    print(ret)

'''104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
