#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import collections
from typing import List
from datatype.tree_node import TreeNode

def postorderTraversal(root: TreeNode) -> List[int]:
    pass

def postorderTraversal_stack(root: TreeNode) -> List[int]:
    """
    栈模拟递归：非递归，中序遍历：左链入栈
    压栈顺序：根"左"右，切入点：右节点前后，一定是左节点后
    """
    result = []
    stack = list()
    prev = None
    while root or len(stack):
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            # None是左节点 == 是右节点
            if not root.right or root.right == prev:
                result.append(root.val)
                prev = root
                root = None
            else:
                # 根节点先弹出再压入
                stack.append(root)
                root = root.right
    return result

def main():

    # root = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # root.setRightNode(n2)
    # n2.setLeftNode(n3)

    root = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n6 = TreeNode(91)
    n7 = TreeNode(92)
    root.setLeftNode(n2)
    root.setRightNode(n3)
    n3.setLeftNode(n4)
    n3.setRightNode(n5)
    n2.setLeftNode(n6)
    n2.setRightNode(n7)

    ret = postorderTraversal(root)
    print(ret)

'''145. 二叉树的后序遍历

给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
