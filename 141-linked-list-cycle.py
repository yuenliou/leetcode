#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode

def hasCycle(head: ListNode) -> bool:
    """
    头尾相接的循环链表：p->next == head
    6型循环链表：内外遍历 > has表(集合/删除) > 双指针(快慢指针)
    双指针问题：翻转链表(前后指针)，获取倒数第k个元素(k间距指针)，获取中间位置的元素(快慢指针)，判断链表是否存在环（快慢指针），判断环的长度(第二次相遇的移动次数)
    """
    fast = slow = head
    # 不同：为什么我们要规定初始时慢指针在位置 head，快指针在位置 head.next，而不是两个指针都在位置 head（即与「乌龟」和「兔子」中的叙述相同）？
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True

    return False

def hasCycle_hash(head: ListNode) -> bool:
    # hash表 比内外循环效率高点
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

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
    node4.next = node2
    ret = hasCycle(node1)
    print(ret)

'''141. 环形链表

给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

 

示例 1：



输入：head = [3,2,0,-4,2], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2,1], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
 

提示：

链表中节点的数目范围是 [0, 104]
-105 <= Node.val <= 105
pos 为 -1 或者链表中的一个 有效索引 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
