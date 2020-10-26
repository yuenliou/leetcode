#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """栈和递归"""
    i = 0
    slow = head
    def removeNthFromEnd_recur(head: ListNode):
        if not head: return
        removeNthFromEnd_recur(head.next)
        nonlocal i; i += 1
        if i == n + 1:
            slow = head #引用不需要nonlocal

    removeNthFromEnd_recur(head)

    if i == n:
        head = head.next
    elif i > n:
        if slow.next:
            slow.next = slow.next.next
    return head

def removeNthFromEnd_point(head: ListNode, n: int) -> ListNode:
    """双指针vs计算长度"""
    fast = slow = head
    i = 0
    while fast:
        fast = fast.next
        i += 1
        if i > n + 1:
            slow = slow.next

    if i == n:
        head = head.next
    elif i > n:
        if slow.next:
            slow.next = slow.next.next
    return head


def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = my_list_node.head
    head = removeNthFromEnd(head, 5)
    while head:
        print(head.val)
        head = head.next

'''19. 删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
