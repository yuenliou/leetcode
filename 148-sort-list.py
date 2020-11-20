#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def sortList(head: ListNode) -> ListNode:
    """快速排序或者归并排序"""
    if not head or not head.next: return head  # termination.
    # cut the LinkedList at the mid index.
    slow, fast = head, head.next
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    mid, slow.next = slow.next, None  # save and cut.
    # recursive for cutting.
    left, right = sortList(head), sortList(mid)
    # merge `left` and `right` linked list and return it.
    h = res = ListNode(0)
    while left and right:
        if left.val < right.val:
            h.next, left = left, left.next
        else:
            h.next, right = right, right.next
        h = h.next
    h.next = left if left else right
    return res.next

def sortList2(head: ListNode) -> ListNode:
    """down2up"""
    h, length, intv = head, 0, 1
    while h: h, length = h.next, length + 1
    res = ListNode(0)
    res.next = head
    # merge the list in different intv.
    while intv < length:
        pre, h = res, res.next
        while h:
            # get the two merge head `h1`, `h2`
            h1, i = h, intv
            while i and h: h, i = h.next, i - 1
            if i: break # no need to merge because the `h2` is None.
            h2, i = h, intv
            while i and h: h, i = h.next, i - 1
            c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
            # merge the `h1` and `h2`.
            while c1 and c2:
                if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                pre = pre.next
            pre.next = h1 if c1 else h2
            while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
            pre.next = h
        intv *= 2
    return res.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(3)

    head = my_list_node.head
    head = sortList(head)
    while head:
        print(head.val)
        head = head.next

'''148. 排序链表

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
