#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import collections
from typing import List
from datatype.tree_node import TreeNode
# 同比任务队列：大才小用了哈哈
from multiprocessing import Queue, SimpleQueue
from queue import Queue, SimpleQueue, LifoQueue, PriorityQueue

def levelOrder(root: TreeNode) -> List[List[int]]:
    """dfs：有level占位，先序中序后续结果都一样"""
    result = []
    def dfs(root, level):
        if not root: return
        if level > len(result): # level = 0; >=/== 可替换
            result.append([])
        temp = result[level - 1]
        # 先序
        temp.append(root.val)
        dfs(root.left, level + 1)
        # 中序
        dfs(root.right, level + 1)
        # 后序
    dfs(root, 1)
    return result

def levelOrder_dfs(root: TreeNode) -> List[List[int]]:
    """dfs"""
    result = []
    def dfs(root, level):
        if root is None: return
        if level < len(result):
            temp = result[level]
        else:
            temp = []
            result.append(temp)
        temp.append(root.val)
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)
    dfs(root, 0)
    # dfs_v2(root, 0, result)
    return result

def dfs_v2(root, level, result):
    if root is None: return
    try:
        temp = result[level]
    except IndexError: #Python的编程理念是“包容错误”而不是“严格检查”
        temp = []
        result.append(temp)
    temp.append(root.val)
    dfs_v2(root.left, level + 1, result)
    dfs_v2(root.right, level + 1, result)

def levelOrder_bfs(root: TreeNode) -> List[List[int]]:
    """bfs"""
    result = list()
    queue = collections.deque()
    queue.append(root)
    while len(queue):# isEmpty()
        temp = []
        # cnt = len(queue); while cnt: ...; cnt -= 1
        for _ in range(len(queue)):
            root = queue.pop() # list.pop(0)
            temp.append(root.val)
            if root.left:
                queue.appendleft(root.left)
            if root.right:
                queue.appendleft(root.right)
        result.append(temp)
    return result

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

    ret = levelOrder(root)
    print(ret)

'''102. 二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
