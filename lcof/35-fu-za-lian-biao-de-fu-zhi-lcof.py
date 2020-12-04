#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    """两步：第一步复制next,第二部复制random"""
    p = head
    dummyCopy = Node(0)
    copy = dummyCopy

    headList = []
    copyList = []
    while p:
        copy.next = Node(p.val)
        copyList.append(copy.next)
        # 深copy这里还是指向原节点的random
        copy.next.random = p.random
        copy = copy.next
        headList.append(p)
        p = p.next

    #遍历解决不了相同元素的问题，map一样，只能用数组记录顺序相对位置
    p = head
    copy = dummyCopy.next
    while p:
        if p.random:
            idx = headList.index(p.random)
            randomCopy = copyList[idx]
            copy.random = randomCopy
        p = p.next
        copy = copy.next

    # return head
    return dummyCopy.next

def copyRandomList1(head: 'Node') -> 'Node':
    """两步：map存储p-copy的映射关系"""
    p = head
    map = {}
    while p:
        node = Node(p.val)
        map[p] = node
        p = p.next

    #此法可优化为一个while：先获取map[p],没有的话直接new
    # https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-by-leetcod/

    # py 一行代码哈哈： copy.deepcopy(head)
    # DFS & BFS
    # https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
    p = head
    while p:
        if p.next:
            map[p].next = map[p.next]
        if p.random:
            map[p].random = map[p.random]
        p = p.next

    return map[head]

def copyRandomList2(head: 'Node') -> 'Node':
    """原地复制：三步：next,random,分离。1->2->3  ==>  1->1'->2->2'->3->3'"""
    #复制next
    p = head
    while p:
        node = Node(p.val)
        node.next = p.next
        p.next = node
        p = p.next.next

    #复制random
    p = head
    while p:
        if p.random:
            p.next.random = p.random.next
        p = p.next.next

    #分离
    p = head
    dummy = Node(0)
    copy = dummy
    while p:
        copy.next = p.next
        copy = copy.next

        p.next = p.next.next
        p = p.next

    return dummy.next

def main():
    node0 = Node(7)
    node1 = Node(13)
    node2 = Node(11)
    node3 = Node(10)
    node4 = Node(1)

    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node0.random = None
    node1.random = node0
    node2.random = node4
    node3.random = node2
    node4.random = node0

    head = copyRandomList2(node0)
    while head:
        print(head.val, head.random.val if head.random else None)
        head = head.next


'''剑指 Offer 35. 复杂链表的复制


给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。


注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
