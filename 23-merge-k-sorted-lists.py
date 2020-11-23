#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.list_node import ListNode, MyListNode


def mergeKLists(lists: List[ListNode]) -> ListNode:
    """
    优先队列:
    元组比较：https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/
    vs 自定义比较函数
    """

    def __lt__(self, other):
        return self.val < other.val

    ListNode.__lt__ = __lt__

    import heapq
    heap = []
    for l in lists:
        if l:
            heapq.heappush(heap, l)

    dummy = ListNode(0)
    p = dummy
    while heap:
        node = heapq.heappop(heap)
        p.next = node
        p = p.next
        if node.next:
            heapq.heappush(heap, node.next)

    return dummy.next


def mergeKLists2(lists: List[ListNode]) -> ListNode:
    """顺序合并"""
    def merge(l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = merge(l1.next, l2)
            return l1
        else:
            l2.next = merge(l1, l2.next)
            return l2
    result = None
    for node in lists:
        result = merge(result, node)
    return result

def mergeKLists1(lists: List[ListNode]) -> ListNode:
    """二分合并"""
    def merge(l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = merge(l1.next, l2)
            return l1
        else:
            l2.next = merge(l1, l2.next)
            return l2

    def mergeArr(arr):
        length = len(arr)
        if length < 1: return None
        if length == 1: return arr[0]

        middle = length // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(mergeArr(left), mergeArr(right))

    return mergeArr(lists)

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)
    l1 = my_list_node.head

    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    l2 = my_list_node.head

    my_list_node = MyListNode()
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(6)
    l3 = my_list_node.head

    head = mergeKLists([l1, l2, l3])
    # head = mergeKLists([[]])
    print(head)
    while head:
        print(head.val)
        head = head.next

'''23. 合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
if __name__ == '__main__':
    main()
