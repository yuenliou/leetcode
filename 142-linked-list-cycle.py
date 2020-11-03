#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

def detectCycle(head: ListNode) -> ListNode:
    """
    头尾相接的循环链表：p->next == head
    6型循环链表：内外遍历 > has表(集合/删除) > 双指针(快慢指针)
    双指针问题：翻转链表(前后指针)，获取倒数第k个元素(k间距指针)，获取中间位置的元素(快慢指针)，判断链表是否存在环（快慢指针），判断环的长度(第二次相遇的移动次数)，入环点
    """

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return slow
    return None

def detectCycle_hash(head: ListNode) -> ListNode:
    # hash表 比内外循环效率高点
    seen = set()
    while head:
        if head in seen:
            return head
        seen.add(head)
        head = head.next
    return None

def main():
    node1 = ListNode(3)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(-4)
    node3.next = node4

    # node5 = ListNode(2)
    # node4.next = node5

    # 链表成环
    node4.next = node2

    #相交节点-4，入环节点2，环长度3
    ret = detectCycle(node1)
    if ret:
        print(ret.val)
    else:
        print(None)


'''142. 环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？
 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
