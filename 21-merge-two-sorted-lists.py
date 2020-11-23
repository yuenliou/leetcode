#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """拓展思路：递归实现"""
    dummyNode = ListNode(0)
    result = dummyNode
    while l1 and l2:
        if l1.val > l2.val:
            result.next = l2
            l2 = l2.next
        else:
            result.next = l1
            l1 = l1.next
        result = result.next

    while l1:
        result.next = l1
        l1 = l1.next
        result = result.next

    while l2:
        result.next = l2
        l2 = l2.next
        result = result.next

    return dummyNode.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(4)

    l1 = my_list_node.head
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    l2 = my_list_node.head

    head = mergeTwoLists(l1, l2)
    while head:
        print(head.val)
        head = head.next

'''21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
