#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def deleteDuplicates(head: ListNode) -> ListNode:
    """解法：重点已排序"""
    dummy = ListNode(0)
    dummy.next = head
    pre, ptr = dummy, head
    while ptr and ptr.next:
        dup = False
        # 找到重复值子链表的最后一个节点
        while ptr and ptr.next and ptr.val == ptr.next.val:
            dup = True
            ptr = ptr.next
        if dup:
            ptr = ptr.next
            pre.next = ptr
        else:
            pre = ptr
            ptr = ptr.next
    return dummy.next

def deleteDuplicates_naive(head: ListNode) -> ListNode:
    """朴素解法：hash表"""
    if not head or not head.next: return head
    ptr, map = head, {}
    while ptr:
        if ptr.val not in map:
            map[ptr.val] = 0
        else:
            map[ptr.val] += 1
        ptr = ptr.next

    dummy = ListNode(0)
    dummy.next = head
    ptr = dummy
    while ptr.next:
        if map[ptr.next.val] > 0:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next
    return dummy.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = deleteDuplicates(my_list_node.head)
    while head:
        print(head.val)
        head = head.next


'''82. 删除排序链表中的重复元素 II

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
