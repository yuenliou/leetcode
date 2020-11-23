#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def swapPairs(head: ListNode) -> ListNode:
    """递归"""
    if not head or not head.next:
        return head
    newHead = head.next
    head.next = swapPairs(newHead.next)
    newHead.next = head
    return newHead

def swapPairs2(head: ListNode) -> ListNode:
    dummyHead = ListNode(0)
    dummyHead.next = head
    temp = dummyHead
    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
    return dummyHead.next

def swapPairs1(head: ListNode) -> ListNode:
    """迭代"""
    dummyNode = ListNode(0)
    p = dummyNode
    while head:
        cur = head
        if cur.next:
            head = cur.next.next
            cur.next.next = cur
            p.next = cur.next
            p = p.next.next
            p.next = None
        else:
            p.next = cur
            head = None
    return dummyNode.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = swapPairs(my_list_node.head)
    while head:
        print(head.val)
        head = head.next

'''24. 两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
