#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    ptr, head_ptr = head, None
    while m > 1:
        m -= 1
        n -= 1
        head_ptr = head
        head = head.next

    between_tail = between_ptr = head

    while n > 0:
        n -= 1
        temp = head.next
        head.next = between_ptr
        between_ptr = head
        head = temp

    between_tail.next = head

    if head_ptr is None:
        ptr = between_ptr
    else:
        head_ptr.next = between_ptr
    return ptr

def reverseBetween_v2(head: ListNode, m: int, n: int) -> ListNode:
    ptr = head_ptr = head
    mm = m
    while m - 1 > 0:
        m -= 1
        head_ptr = head
        head = head.next

    between_tail = between_ptr = head

    while n - mm + 1 > 0:
        n -= 1
        temp = head
        head = head.next
        temp.next = between_ptr
        between_ptr = temp

    between_tail.next = head

    if mm - 2 < 0:
        ptr = between_ptr
    else:
        head_ptr.next = between_ptr
    return ptr

def reverseBetween_v1(head: ListNode, m: int, n: int) -> ListNode:
    """
    1. 这种方法边界情况(i)太复杂
    2. 修改head或者head.next前先保存
    """
    ptr = head_ptr = head
    between_tail = between_ptr = None
    i = 0
    while head and i < n:
        if i == m - 2:
            # 第一段
            head_ptr = head
            head = head.next
        elif i >= m - 1 and i < n:
            # 第二段
            if i == m - 1:
                temp = head
                head = head.next
                between_ptr = temp
                between_tail = between_ptr
            else:
                temp = head
                head = head.next
                temp.next = between_ptr
                between_ptr = temp
        else:
            head = head.next
        i += 1

    between_tail.next = head
    if m - 2 < 0:
        ptr = between_ptr
    else:
        head_ptr.next = between_ptr
    return ptr

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = my_list_node.head
    head = reverseBetween(head, 1, 5)
    while head:
        print(head.val)
        head = head.next

'''92. 反转链表 II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
通过次数82,431提交次数159,609

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
