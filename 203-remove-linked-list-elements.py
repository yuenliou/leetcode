#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def removeElements(head: ListNode, val: int) -> ListNode:
    """模拟题：直接遍历/不用pre节点需要处理end"""
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    cur = head
    while cur:
        if cur.val == val:
            pre.next = cur.next
            cur = pre.next
        else:
            pre = cur
            cur = cur.next
    return dummy.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(6)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(6)

    head = removeElements(my_list_node.head, 6)
    while head:
        print(head.val)
        head = head.next


'''203. 移除链表元素

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-linked-list-elements/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
