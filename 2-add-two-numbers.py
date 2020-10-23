#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    pre = ListNode(0)
    cur = pre

    carry = 0
    while l1 or l2 or carry:
        x =  l1.val if l1 else 0
        y =  l2.val if l2 else 0
        sum = x + y + carry

        cur.next = ListNode(sum % 10)
        cur = cur.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

        # 牛逼2 // -> if
        # carry = sum // 10
        carry =  1 if sum > 9 else 0

    # 牛逼1 or carry
    # if carry: cur.next = ListNode(carry)

    return pre.next


def main():
    node1 = ListNode(2)
    node2 = ListNode(4)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    l1 = node1

    node1 = ListNode(5)
    node2 = ListNode(6)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    l2 = node1

    ret = addTwoNumbers(l1, l2)
    while(ret):
        print(ret.val)
        ret = ret.next


'''2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
