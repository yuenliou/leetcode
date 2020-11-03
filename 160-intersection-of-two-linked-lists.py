#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def getIntersectionNode_iter(headA: ListNode, headB: ListNode) -> ListNode:
    """暴力迭代"""
    while headA:
        hb = headB
        while hb:
            if hb == headA:
                return headA
            hb = hb.next
        headA = headA.next
    return None

def getIntersectionNode_hash(headA: ListNode, headB: ListNode) -> ListNode:
    """hash空间换时间"""
    seen = set()
    while headA:
        seen.add(headA)
        headA = headA.next

    while headB:
        if headB in seen:
            return headB
        headB = headB.next
    return None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    """双指针&拼接->消除长度差"""
    ha, hb = headA, headB
    while ha != hb:
        ha = ha.next if ha else headB
        hb = hb.next if hb else headA
    return ha

def main():
    # 相交部分
    node1 = ListNode(8)
    node2 = ListNode(4)
    node1.next = node2
    node3 = ListNode(5)
    node2.next = node3

    # A
    headA = ListNode(4)
    nodeA1 = ListNode(1)
    headA.next = nodeA1
    nodeA1.next = node1

    # head = headA
    # while head:
    #     print(head.val)
    #     head = head.next

    # B
    headB = ListNode(5)
    nodeB1 = ListNode(0)
    headB.next = nodeB1
    nodeB2 = ListNode(1)
    nodeB1.next = nodeB2
    nodeB2.next = node1

    # head = headB
    # while head:
    #     print(head.val)
    #     head = head.next

    """
    my_list_node = MyListNode()
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(8)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    headA = my_list_node.head

    my_list_node = MyListNode()
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(0)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(8)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    headB = my_list_node.head
    """

    ret = getIntersectionNode(headA, headB)
    if ret:
        print(ret.val)
    else:
        print(None)

'''160. 相交链表


编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
