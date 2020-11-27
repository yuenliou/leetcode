#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def deleteDuplicates(head: ListNode) -> ListNode:
    """解法：重点已排序"""
    if not head or not head.next: return head
    pre, ptr =head, head.next
    while pre and ptr:
        if pre.val == ptr.val:
            pre.next = ptr.next
            ptr = pre.next
        else:
            pre = ptr
            ptr = ptr.next
    return head

def deleteDuplicates_naive(head: ListNode) -> ListNode:
    """朴素解法：hash表"""
    #创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
    pre, ptr, seen =None, head, set()
    while ptr:
        if ptr.val in seen:
            pre.next = ptr.next
            ptr = pre.next
        else:
            seen.add(ptr.val)
            pre = ptr
            ptr = ptr.next
    return head

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(3)

    head = deleteDuplicates(my_list_node.head)
    while head:
        print(head.val)
        head = head.next


'''83. 删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
