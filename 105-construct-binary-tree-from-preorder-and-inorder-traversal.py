#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if (len(preorder) <= 0): return None
    #先序中的第一个元素是根节点
    rootVal = preorder[0]
    idx = inorder.index(rootVal)
    # 构建左右子树
    root = TreeNode(rootVal)
    root.left = buildTree(preorder[1:idx+1], inorder[0:idx]) #0省略
    root.right = buildTree(preorder[idx+1:len(preorder)], inorder[idx+1:len(inorder)]) #len省略
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
