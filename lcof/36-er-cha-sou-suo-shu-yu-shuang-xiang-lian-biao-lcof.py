#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, build_binary_tree, level_order_travel, in_order_travel

class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        """模拟"""
        def inOrder(node):
            if node is None: return
            inOrder(node.left)
            arr.append(node)
            inOrder(node.right)
        arr = []
        inOrder(root)

        size = len(arr)
        if size == 0: return root

        for i in range(size):
            if i == 0:
                arr[i].left = arr[size - 1]
                # 考虑i+1，i-1越界问题
                arr[i].right = arr[0] if i + 1 == size else arr[i + 1]
            elif i == size - 1:
                arr[i].left = arr[i - 1]
                arr[i].right = arr[0]
            else:
                arr[i].left = arr[i - 1]
                arr[i].right = arr[i + 1]

        return arr[0]

    def treeToDoublyList1(self, root: TreeNode) -> TreeNode:
        """递归：根据以上分析，考虑使用[中序遍历]访问树的各节点 cur ；并在访问每个节点时构建 cur 和前驱节点 pre 的引用指向；中序遍历完成后，最后构建头节点和尾节点的引用指向即可。"""
        def dfs(cur):
            nonlocal pre, head
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if pre:  # 修改节点引用
                pre.right, cur.left = cur, pre
            else:  # 记录头节点
                head = cur
            pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return root
        head = pre = None
        dfs(root)
        head.left, pre.right = pre, head
        return head

def main():

    root = build_binary_tree([4,2,5,1,3])
    print('-level-')
    level_order_travel(root)
    print('-in-')
    in_order_travel(root)

    solution = Solution()
    ret = solution.treeToDoublyList1(root)

    print('->right>-')
    #右循环
    head = ret
    while head:
        print(head.val)
        if head.right == ret: break
        head = head.right

    print('-<left<-')
    #左循环
    head = ret.left
    while head:
        print(head.val)
        if head.left == ret.left: break
        head = head.left

'''剑指 Offer 36. 二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 



 

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 



 

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

 

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
