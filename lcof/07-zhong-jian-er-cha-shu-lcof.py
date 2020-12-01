#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if (len(preorder) <= 0): return None
    # 先序中的第一个元素是根节点
    rootVal = preorder[0]
    idx = inorder.index(rootVal)
    # 构建左右子树
    root = TreeNode(rootVal)
    root.left = buildTree(preorder[1:idx + 1], inorder[0:idx])
    root.right = buildTree(preorder[idx + 1:len(preorder)], inorder[idx + 1:len(inorder)])
    return root

def main():
    """
    思路1.先序遍历的第一个元素是root，中序遍历root节点之前的是左子树，之后是右子树，递归求解
    """
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    ret = buildTree(preorder, inorder)
    print('-pre-')
    pre_order_travel(ret)
    print('-in-')
    in_order_travel(ret)
    print('-post-')
    post_order_travel(ret)

'''剑指 Offer 07. 重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
