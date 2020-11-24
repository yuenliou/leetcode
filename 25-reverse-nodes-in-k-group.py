#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """图解k个一组翻转链表：
    一图胜千言：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/tu-jie-kge-yi-zu-fan-zhuan-lian-biao-by-user7208t/
    """
    def reverse(head):
        """翻转链表"""
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    dummyNode = ListNode(0)
    dummyNode.next = head

    # 初始pre/end
    pre = dummyNode
    end = pre

    while end.next:
        for _ in range(k):
            end = end.next
            if not end:
                return dummyNode.next
        #记录start
        start = pre.next
        #记录next
        next = end.next
        #断开k区间的链表
        end.next = None
        #翻转
        pre.next = reverse(start)
        #拼接翻转之后的k区间
        start.next = next
        #重置pre/end
        pre = start
        end = pre
    return dummyNode.next

def reverseKGroup1(head: ListNode, k: int) -> ListNode:
    def reverse(head, tail):
        """翻转一个子链表，并且返回新的头与尾"""
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    dummyNode = ListNode(0)
    dummyNode.next = head
    pre = dummyNode

    while head:
        tail = pre
        # 查看剩余部分长度是否大于等于 k
        for _ in range(k):
            tail = tail.next
            if not tail:
                return dummyNode.next

        nex = tail.next
        head, tail = reverse(head, tail)
        # 把子链表重新接回原链表
        pre.next = head
        tail.next = nex
        pre = tail
        head = tail.next
    return dummyNode.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)

    head = reverseKGroup(my_list_node.head, 2)
    while head:
        print(head.val)
        head = head.next

'''25. K 个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
