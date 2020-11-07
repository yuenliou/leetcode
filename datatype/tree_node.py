#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def getValue(self):
        return self.val

    def setLeftNode(self, left):
        self.left = left

    def getLeftNode(self):
        return self.left

    def setRightNode(self, right):
        self.right = right

    def getRightNode(self):
        return self.right

    def setParentNode(self, parent):
        self.parent = parent

    def getParentNode(self):
        return self.parent

def build_tree_node(arr):
    """构建任意二叉树"""
    pass

def build_bst(arr):
    """
    构建二叉搜索树/二叉平衡树/完全二叉树
    方法3： 中序遍历策略带来的优化
    https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/shou-hua-tu-jie-san-chong-jie-fa-jie-zhu-shu-zu-ku/
    """
    def build(start, end):
        if start > end: return None
        mid = (start + end + 1) >> 1
        root = TreeNode(arr[mid])
        root.left = build(start, mid - 1)
        root.right = build(mid + 1, end)
        return root
    return build(0, len(arr) - 1)

def pre_order_travel(node: TreeNode):
    """先序遍历"""
    if node is None: return
    print(node.val)
    pre_order_travel(node.left)
    pre_order_travel(node.right)

def in_order_travel(node: TreeNode):
    """中序遍历"""
    if node is None: return
    in_order_travel(node.left)
    print(node.val)
    in_order_travel(node.right)

def post_order_travel(node: TreeNode):
    """后序遍历"""
    if node is None: return
    post_order_travel(node.left)
    post_order_travel(node.right)
    print(node.val)

def tree_node_test():
    pass

if __name__ == '__main__':
    # root = build_bst([-10, -3, 0, 5, 9])
    # in_order_travel(root)
    # root = build_bst([1, 3, 2])
    # in_order_travel(root)

    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.setRightNode(n2)
    n2.setLeftNode(n3)
    in_order_travel(root)


