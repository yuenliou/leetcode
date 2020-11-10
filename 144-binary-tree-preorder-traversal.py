#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import collections
from typing import List
from datatype.tree_node import TreeNode


def preorderTraversal(root: TreeNode) -> List[int]:
    """
    栈：先进后出
    入栈顺序：右左，
    出站顺序：左右。
    """
    if not root: return []
    res, stack = [], [root]
    while stack:
        cur = stack.pop()
        # 先序
        # [3, 9, 91, 92, 20, 15, 7]
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        """接下来我们思考一下前序遍历和后序遍历之间的关系：
        前序遍历顺序为：根 -> 左 -> 右
        后序遍历顺序为：左 -> 右 -> 根
        如果1： 我们将前序遍历中节点插入结果链表尾部的逻辑，修改为将节点插入结果链表的头部
        那么结果链表就变为了：右 -> 左 -> 根
        如果2： 我们将遍历的顺序由从左到右修改为从右到左，配合如果1
        那么结果链表就变为了：左 -> 右 -> 根
        这刚好是后序遍历的顺序
        基于这两个思路，我们想一下如何处理：
        修改前序遍历代码中，节点写入结果链表的代码，将插入队尾修改为插入队首
        修改前序遍历代码中，每次先查看左节点再查看右节点的逻辑，变为先查看右节点再查看左节点
        """
        # 后序：1.入栈顺序不同，2.插入方向相反。
        '''下面*_stack的先序也可以这么写，严格意义上不符合遍历顺序，只是最终结果一样'''
        # [91, 92, 9, 15, 7, 20, 3]
        # res.insert(0, cur.val)
        # if cur.left:
        #     stack.append(cur.left)
        # if cur.right:
        #     stack.append(cur.right)
    return res


def preorderTraversal_stack(root: TreeNode) -> List[int]:
    """
    栈模拟递归：非递归，中序遍历：左链入栈
    压栈顺序：根"左"右，切入点：根前后，一定是左节点前
    """
    result = []
    stack = list()
    while root or len(stack):
        if root:
            # 先序
            result.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            # 中序
            root = root.right

    return result

def preorderTraversal_recur(root: TreeNode) -> List[int]:
    """递归"""
    if not root:
        return []
    return [root.val] + preorderTraversal_recur(root.left) + preorderTraversal_recur(root.right)


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

    """    3
          /   \
         9    20
        /  \  /  \
       91  92  15  7
    """
    ret = preorderTraversal(root)
    print(ret)

'''144. 二叉树的前序遍历

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
