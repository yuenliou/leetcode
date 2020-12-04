#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.list_node import ListNode, MyListNode


def removeZeroSumSublists(head: ListNode) -> ListNode:
    """前缀和+hashmap：sum相同的节点后面会覆盖前面，二次遍历间接删除了sum=0的节点"""
    dummy = ListNode(0)
    dummy.next = head

    sum_map = dict()
    p, sum_value = dummy, 0
    while p:
        sum_value += p.val
        sum_map[sum_value] = p
        p = p.next
        
    p, sum_value = dummy, 0
    while p:
        sum_value += p.val
        p.next = sum_map[sum_value].next
        p = p.next
        
    return dummy.next

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(-3)
    my_list_node.addAtTail(4)

    head = removeZeroSumSublists(my_list_node.head)
    while head:
        print(head.val)
        head = head.next

'''1171. 从链表中删去总和值为零的连续节点

给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

 

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]
 

提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
