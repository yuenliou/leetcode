#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    n = len(preorder)
    # 构造哈希映射，帮助我们快速定位根节点
    index = {element: i for i, element in enumerate(inorder)}

    def build(preorder_left, preorder_right, inorder_left, inorder_right) -> TreeNode:
        if (preorder_left > preorder_right): return None

        # 前序遍历中的第一个节点就是根节点
        preorder_root = preorder_left
        # 在中序遍历中定位根节点
        inorder_root = index[preorder[preorder_root]]

        # 先把根节点建立出来
        root = TreeNode(preorder[preorder_root])
        # 得到左子树中的节点数目
        size_left_subtree = inorder_root - inorder_left
        # 递归地构造左子树，并连接到根节点
        # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
        root.left = build(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
        # 递归地构造右子树，并连接到根节点
        # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
        root.right = build(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
        return root
    return build(0, n - 1, 0, n - 1)


def buildTree_recur(preorder: List[int], inorder: List[int]) -> TreeNode:
    if (len(preorder) <= 0): return None
    #先序中的第一个元素是根节点
    rootVal = preorder[0]
    idx = inorder.index(rootVal)
    # 构建左右子树
    root = TreeNode(rootVal)
    root.left = buildTree_recur(preorder[1:idx+1], inorder[0:idx]) #0省略
    root.right = buildTree_recur(preorder[idx+1:len(preorder)], inorder[idx+1:len(inorder)]) #len省略
    return root

def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    ret = buildTree(preorder, inorder)
    print('-pre-')
    pre_order_travel(ret)
    print('-in-')
    in_order_travel(ret)
    print('-post-')
    post_order_travel(ret)

'''105. 从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
