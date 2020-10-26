#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def deleteNode(node: ListNode):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    #不能删除当前节点，那就交换下一个节点的值然后删除下一个节点
    node.val = node.next.val
    node.next = node.next.next

def main():
    node1 = ListNode(4)
    node2 = ListNode(5)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    node4 = ListNode(9)
    node3.next = node4

    deleteNode(node2)
    head = node1
    while head:
        print(head.val)
        head = head.next

'''237. 删除链表中的节点

copy from leetcode

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

 

现有一个链表 -- head = [4,5,1,9]，它可以表示为:



 

示例 1：

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2：

输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

提示：

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
