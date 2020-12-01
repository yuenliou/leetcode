#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def reverseList(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

def main():
    """
    思路1.迭代&双指针&头插法&尾插法
    思路2.递归，栈不常用
    """
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = reverseList(my_list_node.head)
    while head:
        print(head.val)
        head = head.next

'''剑指 Offer 24. 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

 

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
