#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, in_order_travel


def inorderTraversal_morris(root: TreeNode) -> List[int]:
    """
    莫里斯遍历：用递归和迭代的方式都使用了辅助的空间，而莫里斯遍历的优点是没有使用任何辅助空间。
               缺点是改变了整个树的结构，强行把一棵二叉树改成一段链表结构。
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
    """
    res = []
    while root:
        if root.left:
            # 第一部分：左子树的最右节点挂root
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root

            # 第二部分：root指向root的left
            tmp = root
            root = root.left

            # 第三部分：去掉root到root.left前的left
            tmp.left = None
        else:
            res.append(root.val)
            root = root.right
    return res

def inorderTraversal(root: TreeNode) -> List[int]:
    """
    颜色标记法-一种通用且简明的树遍历方法
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码。
    解释一下为什么需要“右子节点、自身、左子节点依次入栈”?
    因为栈是一种 先进后出的结构，出栈顺序为左，中，右，那么入栈顺序必须调整为倒序，也就是右，中，左
    同理，如果是前序遍历，入栈顺序为 右，左，中；后序遍历，入栈顺序中，右，左
    """
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None: continue
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)
    return res

def inorderTraversal_color_v2(root: TreeNode) -> List[int]:
    """
    大佬的方法还可以优化：
    white对应TreeNode数据类型，gray对应int数据类型，所以不需要额外的颜色标记：
    """
    stack, rst = [root], []
    while stack:
        i = stack.pop()
        if isinstance(i, TreeNode):
            stack.extend([i.right, i.val, i.left])
        elif isinstance(i, int):
            rst.append(i)
    return rst


def inorderTraversal_stack(root: TreeNode) -> List[int]:
    """栈模拟递归：非递归，中序遍历：左链入栈"""
    result = []
    stack = list()
    while root or len(stack):
        if root: #while替换
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)
            root = root.right

    return result

def inorderTraversal_recur(root: TreeNode) -> List[int]:
    result = []
    def in_order(root):
        if root is None: return
        in_order(root.left)
        result.append(root.val)
        in_order(root.right)
    in_order(root)
    return result

def main():

    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.setRightNode(n2)
    n2.setLeftNode(n3)

    ret = inorderTraversal(root)
    print(ret)

'''94. 二叉树的中序遍历

给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
