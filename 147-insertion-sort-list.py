#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode


def insertionSortList(head: ListNode) -> ListNode:
    """对于单向链表而言，只有指向后一个节点的指针，因此需要从链表的头节点开始往后遍历链表中的节点，寻找插入位置。"""
    if not head:
        return head

    dummyHead = ListNode(0)
    dummyHead.next = head
    lastSorted = head
    curr = head.next

    while curr:
        if lastSorted.val <= curr.val:
            lastSorted = lastSorted.next
        else:
            prev = dummyHead
            while prev.next.val <= curr.val:
                prev = prev.next
            lastSorted.next = curr.next
            curr.next = prev.next
            prev.next = curr
        curr = lastSorted.next

    return dummyHead.next

def insertionSortList2(head: ListNode) -> ListNode:
    if not head: return head
    dummy = ListNode()
    dummy.next = head
    cur_pre = head
    cur = head.next
    while cur:
        # 直接下一个
        if cur.val >= cur_pre.val:
            cur_pre = cur
            cur = cur.next
        else: # 一定会有一个比cur大的节点
            greater_pre = dummy
            while greater_pre.next.val <= cur.val:
                greater_pre = greater_pre.next

            #这是和官方有出入的地方
            temp = cur.next

            #插入
            cur.next = greater_pre.next
            greater_pre.next = cur

            #下一个
            cur = temp
            cur_pre.next = cur

    return dummy.next

def insertionSortList1(head: ListNode) -> ListNode:
    if not head: return head
    dummy = ListNode()
    dummy.next = head
    cur_pre = head
    cur = head.next
    while cur:
        # 直接下一个
        if cur.val >= cur_pre.val:
            cur_pre = cur
            cur = cur.next
        else: # 一定会有一个比cur大的节点
            h = dummy.next
            greater = None
            while h and h.next != cur:
                if cur.val >= h.val and cur.val <= h.next.val:
                    # 记录先不交换
                    greater = h
                h = h.next

            temp = cur.next

            # 插入cur
            if greater:
                cur.next = greater.next
                greater.next = cur
            else:
                cur.next = dummy.next
                dummy.next = cur

            # 删除cur
            cur = temp
            cur_pre.next = cur

    return dummy.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(3)

    head = my_list_node.head
    head = insertionSortList2(head)
    while head:
        print(head.val)
        head = head.next

'''147. 对链表进行插入排序

对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
