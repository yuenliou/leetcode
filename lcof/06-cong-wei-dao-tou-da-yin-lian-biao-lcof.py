#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.list_node import ListNode, MyListNode


def reversePrint(head: ListNode) -> List[int]:
    return reversePrint(head.next) + [head.val] if head else []

def reversePrint3(head: ListNode) -> List[int]:
    list = []
    def reverse(head: ListNode):
        if not head: return
        reverse(head.next)
        list.append(head.val)
    reverse(head)
    return list

def reversePrint2(head: ListNode) -> List[int]:
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    # list = []
    # while len(stack):
    #     list.append(stack.pop())
    return stack[::-1]

def reversePrint1(head: ListNode) -> List[int]:
    def reverse(head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    list = []
    head = reverse(head)
    while head:
        list.append(head.val)
        head = head.next
    return list

def main():
    """
    思路1.翻转链表
    思路2.栈
    思路3.递归
    """
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    ret = reversePrint(my_list_node.head)
    print(ret)


'''剑指 Offer 06. 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
