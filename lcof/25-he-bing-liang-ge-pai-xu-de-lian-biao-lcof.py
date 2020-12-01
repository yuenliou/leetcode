#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeTwoLists1(l1: ListNode, l2: ListNode) -> ListNode:
    """拓展思路：递归实现"""
    dummyNode = ListNode(0)
    result = dummyNode
    while l1 and l2:
        if l1.val > l2.val:
            result.next = l2
            l2 = l2.next
        else:
            result.next = l1
            l1 = l1.next
        result = result.next

    # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    result.next = l1 if l1 is not None else l2

    # while l1:
    #     result.next = l1
    #     l1 = l1.next
    #     result = result.next
    #
    # while l2:
    #     result.next = l2
    #     l2 = l2.next
    #     result = result.next

    return dummyNode.next


def main():
    """
    思路1.类似于归并排序的merge函数
    思路2.递归不常用
    """
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(4)

    l1 = my_list_node.head
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    l2 = my_list_node.head

    head = mergeTwoLists(l1, l2)
    while head:
        print(head.val)
        head = head.next

'''剑指 Offer 25. 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
