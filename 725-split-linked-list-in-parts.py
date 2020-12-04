#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.list_node import ListNode, MyListNode

def splitListToParts(root: ListNode, k: int) -> List[ListNode]:
    p = root
    cnt = 0
    while p:
        cnt += 1
        p = p.next

    # mod = cnt % k
    # c = cnt // k
    c , mod = divmod(cnt, k)

    #数组中链表长度
    gcnt = [0] * k
    for i in range(k):
        gcnt[i] = c + (1 if mod > 0 else 0)
        mod -= 1

    """ 不构建上面的gcnt数组
        width, remainder = divmod(N, k)
        ...
            for j in xrange(width + (i < remainder) - 1):
                if cur: cur = cur.next
    """

    print(gcnt)
    #根据每个定义的链表长度进行截取
    p = root
    res = []
    for i in gcnt:
        if not p:
            res.append(None)
            continue
        pre = p
        while i > 1:
            i -= 1
            p = p.next

        next = p.next
        p.next = None
        res.append(pre)
        pre = next
        p = pre

    return res

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)
    my_list_node.addAtTail(5)
    my_list_node.addAtTail(6)
    my_list_node.addAtTail(7)

    ret = splitListToParts(my_list_node.head, 3)

    for head in ret:
        while head:
            print(head.val)
            head = head.next


'''725. 分隔链表

给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例 1：

输入: 
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。
例如, 输入的结点 root 的 val= 1, root.next.val = 2, root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
示例 2：

输入: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
 

提示:

root 的长度范围： [0, 1000].
输入的每个节点的大小范围：[0, 999].
k 的取值范围： [1, 50].


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-linked-list-in-parts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
