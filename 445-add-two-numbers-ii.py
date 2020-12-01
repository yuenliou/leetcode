#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    #栈1
    stack1 = []
    while l1:
        stack1.append(l1)
        l1 = l1.next
    #栈2
    stack2 = []
    while l2:
        stack2.append(l2)
        l2 = l2.next

    #求和
    carry = 0
    # stack3 = []
    head = None
    while len(stack1) or len(stack2) or carry:
        x =  stack1.pop().val if len(stack1) else 0
        y =  stack2.pop().val if len(stack2) else 0
        sum = x + y + carry
        # stack3.append(ListNode(sum % 10))
        node = ListNode(sum % 10)
        node.next = head
        head = node
        carry = sum // 10

    #结果栈
    # dummy = ListNode(0)
    # cur = dummy
    # while len(stack3):
    #     cur.next = stack3.pop()
    #     cur = cur.next
    # return dummy.next
    return head

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(7)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(3)

    l1 = my_list_node.head
    my_list_node = MyListNode()
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(6)
    my_list_node.addAtTail(4)
    l2 = my_list_node.head

    head = addTwoNumbers(l1, l2)
    while head:
        print(head.val)
        head = head.next


'''445. 两数相加 II

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
