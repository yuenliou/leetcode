#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.list_node import ListNode, MyListNode


def numComponents(head: ListNode, G: List[int]) -> int:
    """
    1，由于数组G是链表head所有元素值的子集，所以数组G中的任何元素都能在链表中找到（这TM不是废话？）;
    2，因此G中的每个元素就可以看做是链表head的一个子链表，即G中的每个元素都是链表head的组件；
    3，但是此时的组件还不敢称之为真正的组件，因为完全存在这样一种可能：
       3.1 G中任意组合的两个元素a, b构成了一个更长的head的子链表 a->b ，
       3.2 此时根据题意 a->b 比 a 和 b 都要长，所以 a->b 包涵了 a、b 成为真正的组件，原来的a、b 就不能算组件了，
       3.3 如此一来问题变成了 对于给定的集合G，G中所有的元素能构成多少个head中相连的子链表？
    线性扫描：https://leetcode-cn.com/problems/linked-list-components/solution/lian-biao-zu-jian-by-leetcode/
    """
    Gset = set()
    for n in G:
        Gset.add(n)

    count, p = 0, head
    while p:
        if p.val in Gset and (not p.next or p.next.val not in Gset):
            count += 1
        p = p.next
    return count

def main():
    my_list_node = MyListNode()
    my_list_node.addAtTail(0)
    my_list_node.addAtTail(1)
    my_list_node.addAtTail(2)
    my_list_node.addAtTail(3)
    my_list_node.addAtTail(4)

    ret = numComponents(my_list_node.head, [0, 3, 1, 4])
    print(ret)


'''817. 链表组件

给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。

同时给定列表 G，该列表是上述链表中整型值的一个子集。

返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。

 

示例 1：

输入: 
head: 0->1->2->3
G = [0, 1, 3]
输出: 2
解释: 
链表中,0 和 1 是相连接的，且 G 中不包含 2，所以 [0, 1] 是 G 的一个组件，同理 [3] 也是一个组件，故返回 2。
示例 2：

输入: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
输出: 2
解释: 
链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
 

提示：

如果 N 是给定链表 head 的长度，1 <= N <= 10000。
链表中每个结点的值所在范围为 [0, N - 1]。
1 <= G.length <= 10000
G 是链表中所有结点的值的一个子集.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-components
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
