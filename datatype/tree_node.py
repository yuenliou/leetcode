#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    tree_node_test()
