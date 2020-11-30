#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def deleteNode(head: ListNode, val: int) -> ListNode:
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

def deleteNode_recur(head: ListNode, val: int) -> ListNode:
    if not head or not head.next: return head
    if head.val == val: return head.next
    head.next = deleteNode_recur(head.next, val)
    return head

def main():
    """
    思路1.哑结点+双指针
    思路2.递归不常用
    """
    my_list_node = MyListNode()
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(9)

    head = deleteNode(my_list_node.head, 5)
    while head:
        print(head.val)
        head = head.next

'''剑指 Offer 18. 删除链表的节点

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
