#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def rotateRight(head: ListNode, k: int) -> ListNode:
    """技巧skill解法：循环链表"""
    if not head: return head
    tail, p = None, head
    length = 0
    while p: length, tail, p = length + 1, p, p.next

    # 总长度取余
    idx = length - k % length
    if idx == length: return head

    # 成环，head - tail = 1
    tail.next = head
    i = 0
    while i < idx:
        i += 1
        head = head.next
        tail = tail.next
    # 旋转k，head走length-k步
    tail.next = None
    return head

def rotateRight_naive(head: ListNode, k: int) -> ListNode:
    """朴素解法：截断+拼接"""
    if not head: return head
    tail, p1 = None, head
    length = 0
    while p1:
        length += 1
        tail = p1
        p1 = p1.next

    # 总长度取余
    idx = length - k % length
    if idx == length: return head

    # 截成两段p1，p2
    p2 = l1 = head
    i, l2 = 0, None
    while p2:
        if i == idx - 1:
            l2 = p2.next
            p2.next = None
            break
        i += 1
        p2 = p2.next

    tail.next = l1
    return l2

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = rotateRight(my_list_node.head, 1)
    while head:
        print(head.val)
        head = head.next

'''61. 旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
