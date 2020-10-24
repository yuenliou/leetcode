#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode

def isPalindrome(head: ListNode) -> bool:
    """
    思路：我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。比较完成后我们应该将链表恢复原样。
    算法流程可以分为以下五个步骤：
        1.找到前半部分链表的尾节点。
        2.反转后半部分链表。
        3,判断是否回文。
        4.恢复链表。
        5.返回结果。
    :param head:
    :return:
    """
    if head is None:
        return True

    # 找到前半部分链表的尾节点并反转后半部分链表
    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(first_half_end.next)

    # 判断是否回文
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # 还原链表并返回结果
    first_half_end.next = reverse_list(second_half_start)
    return result

def end_of_first_half(head):
    # 双指针中位
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse_list(head):
    # 翻转链表
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def isPalindrome_recur(head: ListNode) -> bool:
    """
    堆栈帧的开销很大
    :param head:
    :return:
    """
    front_pointer = head
    def recursively_check(current_node=head):
        nonlocal front_pointer
        if current_node:
            if not recursively_check(current_node.next):
                return False
            if front_pointer.val != current_node.val:
                return False
            front_pointer = front_pointer.next
        return True

    return recursively_check()

def isPalindrome_iter(head: ListNode) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]

def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    # node4 = ListNode(1)
    # node3.next = node4
    ret = isPalindrome(node1)
    print(ret)


'''234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
