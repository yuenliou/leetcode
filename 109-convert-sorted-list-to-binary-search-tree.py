#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel


def sortedListToBST(head: ListNode) -> TreeNode:
    if head is None: return None
    if head.next is None: return TreeNode(head.val)

    fast = slow = prev = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # 根据中间节点一分为二
    prev.next = None
    head2 = slow.next

    node = TreeNode(slow.val)
    node.left = sortedListToBST(head)
    node.right = sortedListToBST(head2)
    return node

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(-10)
    my_list_node.addAtTail(-3)
    my_list_node.addAtTail(0)
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(9)

    head = my_list_node.head
    head = sortedListToBST(head)
    print('-pre-')
    pre_order_travel(head)
    print('-in-')
    in_order_travel(head)
    print('-post-')
    post_order_travel(head)

'''109. 有序链表转换二叉搜索树

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
