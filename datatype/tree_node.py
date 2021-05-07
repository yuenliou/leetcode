#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from collections import deque

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

def build_binary_tree(arr):
    """构建任意二叉树：层序"""
    def build(arr):
        length = len(arr)
        if length <= 0: return None
        #根节点
        root = TreeNode(arr[0])
        queue = deque()
        queue.append(root)
        #一层循环，不同于遍历
        for i in range(1, length, 2):
            node = queue.popleft() # 左出右进
            if arr[i]:
                left = TreeNode(arr[i])
                node.setLeftNode(left)
                queue.append(left) # 左出右进
            if i + 1 == length: break
            if arr[i + 1]:
                right = TreeNode(arr[i + 1])
                node.setRightNode(right)
                queue.append(right) # 左出右进
        return root
    return build(arr)

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

def build_bst2(arr):
    """上述构建二叉搜索树限制：必须是有序数组 ??? 此处存疑 ???"""
    def build(start, end):
        if start > end: return None
        pivotIndex = partition(arr, start, start, end)
        root = TreeNode(arr[pivotIndex])
        root.left = build(start, pivotIndex - 1)
        root.right = build(pivotIndex + 1, end)
        return root
    return build(0, len(arr) - 1)

def partition(arr, pivot, left, right):
    """双指针分区：应用快速排序，构建二叉搜索树，在 O(n) 的时间复杂度内求无序数组的第k大元素"""
    i = left
    j = right
    pivotVal = arr[pivot]
    #左右指针相遇的时候退出扫描循环
    while i < j:
        #思考：为什么是右指针先扫而不是左指针先扫呢，大家自己想想吧哈哈，模拟一下就知道了
        while i < j and arr[j] >= pivotVal:
            j -= 1  # 从右向左找第一个小于x的数
        # if (i < j):
        # 	arr[i] = arr[j];i += 1
        while i < j and arr[i] <= pivotVal:
            i += 1 # 从左向右找第一个大于x的数
        # if (i < j):
        # 	arr[j] = arr[i];j -= 1
        # 交换左右指针所停位置的数
        [arr[i], arr[j]] = [arr[j], arr[i]];
    # 最后交换基准数与指针相遇位置的数：只有先进行右指针的运动，才可以保证在相遇处的数字小于基准数
    [arr[pivot], arr[i]] = [arr[i], arr[pivot]];
    # arr[i] = pivotVal
    return i

def pre_order_travel(root: TreeNode):
    """先序遍历"""
    def preOrder(node):
        if node is None: return
        list.append(node.val)
        preOrder(node.left)
        preOrder(node.right)
    list = []
    preOrder(root)
    print('pre-order', list, sep=': ')

def in_order_travel(root: TreeNode):
    """中序遍历"""
    def inOrder(node):
        if node is None: return
        inOrder(node.left)
        list.append(node.val)
        inOrder(node.right)
    list = []
    inOrder(root)
    print('in-order', list, sep=': ')

def post_order_travel(root: TreeNode):
    """后序遍历"""
    def postOrder(node):
        if node is None: return
        postOrder(node.left)
        postOrder(node.right)
        list.append(node.val)
    list = []
    postOrder(root)
    print('post-order', list, sep=': ')

def level_order_travel(node: TreeNode):
    """层序遍历"""
    if not node: return
    queue = deque()
    queue.append(node)
    while len(queue):# isEmpty()
        # cnt = len(queue); while cnt: ...; cnt -= 1
        for _ in range(len(queue)):
            # 右出左进
            root = queue.pop() # list.pop(0)
            print(root.val)
            if root.left:
                queue.appendleft(root.left)
            if root.right:
                queue.appendleft(root.right)


def tree_node_test():
    pass

if __name__ == '__main__':
    # root = build_bst([1, 3, 2])
    # in_order_travel(root)

    root = build_bst([-10, -3, 0, 5, 9])
    pre_order_travel(root)
    in_order_travel(root)
    post_order_travel(root)

    root = build_bst2([-10, -3, 0, 5, 9])
    pre_order_travel(root)
    in_order_travel(root)
    post_order_travel(root)

    root = build_bst2([0, 5, -3, 9, -10])
    pre_order_travel(root)
    in_order_travel(root)
    post_order_travel(root)

    # root = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # root.setRightNode(n2)
    # n2.setLeftNode(n3)
    # in_order_travel(root)

    # root = build_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    # print('-level-')
    # level_order_travel(root)



