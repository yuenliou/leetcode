#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    if not head:
        return

    vec = list()
    node = head
    while node:
        vec.append(node)
        node = node.next

    i, j = 0, len(vec) - 1 #这个写法学习一下哈哈
    while i < j:
        vec[i].next = vec[j]
        i += 1
        if i == j:
            break
        vec[j].next = vec[i]
        j -= 1

    vec[i].next = None
# fisrt zhazha noodles
def reorderList_byNoodles(head: ListNode) -> None:
    if not head:
        return
    list = []
    # 正序列表当栈用
    stack = []
    # POP列表当FIFO队列用
    queue = []

    node = head
    while(node.next is not None):
        list.append(node)
        node = node.next
    list.append(node)

    l = len(list)
    mod = l % 2
    mid = l // 2
    mid += mod
    stack = list[:mid]
    queue = list[mid:]

    head = None
    lastNode = None
    # 可以用双指针
    for i, s_node in enumerate(stack):
        if i == 0:
            # head = s_node # 冗余的复制
            lastNode = s_node
        else:
            lastNode.next = s_node
            lastNode = lastNode.next

        try:
            q_node = queue.pop()
            lastNode.next = q_node
            lastNode = lastNode.next
        except:
            pass

    lastNode.next = None

def main():
    flag = False
    if flag:
        last = ListNode(5)
        node4 = ListNode(4, last)
        node3 = ListNode(3, node4)
        node2 = ListNode(2, node3)
        head = ListNode(1, node2)
    else:
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node3 = ListNode(3)
        node2.next = node3
        last = ListNode(4)
        node3.next = last

    curNode = head
    while(curNode.next is not None):
        print(curNode.val)
        curNode = curNode.next
    print(curNode.val)

    reorderList_byNoodles(head)
    print('----------')

    while(head):
        print(head.val)
        head = head.next


'''143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
