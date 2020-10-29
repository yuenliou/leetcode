#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def partition(head: ListNode, x: int) -> ListNode:
    biggerHead = bigger = ListNode()
    smallerHead = smaller = ListNode()
    while head:
        if  head.val < x:
            smaller.next = head
            smaller = smaller.next
        else:
            bigger.next = head
            bigger = bigger.next
        head = head.next
    smaller.next = biggerHead.next
    bigger.next = None
    return smallerHead.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(2)

    head = my_list_node.head
    head = partition(head, 3)
    while head:
        print(head.val)
        head = head.next

'''86. 分隔链表

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

 

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
