#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 尾插法
def reverseList(head: ListNode) -> ListNode:
    if head == None: return head
    end = head

    while head.next:
        head = head.next

    while end != head:
        temp = end
        end = end.next
        temp.next = head.next
        head.next = temp

    return head

# 迭代&双指针&头插法
def reverseList_iteration(head: ListNode) -> ListNode:
    pre = None
    cur = head
    # next = None
    while cur:
        # next = cur.next # nextTemp
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

# 栈
def reverseList_stack(head: ListNode) -> ListNode:
    if head == None: return head

    stack = list()
    while head:
        stack.append(head)
        head = head.next

    head = stack.pop()
    temp = head
    while len(stack):
        node = stack.pop()
        temp.next = node
        temp = temp.next

    temp.next = None
    return head

# 递归
def reverseList_recursion(head: ListNode) -> ListNode:
    if head == None or head.next is None:
        return head
    node = reverseList_recursion(head.next)
    head.next.next = head
    head.next = None
    return node

def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5

    # 不考虑憨憨解法之"数组赋值"
    ret = reverseList(node1)
    while(ret):
        print(ret.val)
        ret = ret.next

'''206. 反转链表

反转一个单链表。

示例:

输入: 1->2->3->4->5->None
输出: 5->4->3->2->1->None
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
