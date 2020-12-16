#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.list_node import ListNode, MyListNode

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        #构造一个循环链表
        my_list_node = MyListNode()
        for i in range(n):
            my_list_node.addAtTail(i)

        head = my_list_node.head
        p, tail = head, None
        while p:
            tail = p
            p = p.next
        #成环
        tail.next = head

        #模拟
        cnt = 0
        p = head
        while p.next != p:
            # print(p.val)
            cnt += 1
            if cnt == m - 1:
                p.next = p.next.next
                cnt = 0
            else:
                p = p.next
        return p.val

    def lastRemaining1(self, n: int, m: int) -> int:
        #f(n) = f(n-1) + m % n
        def f(n, m):
            if n == 1: return 0
            return (f(n - 1, m) + m) % n
        return f(n, m)

    def lastRemaining2(self, n: int, m: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            ans = (ans + m) % i
        return ans

def main():
    """
    思路1.链表
    思路2.递归
    思路3.数学
    """
    param = 5
    param2 = 3
    solution = Solution()
    ret = solution.lastRemaining(param, param2)
    print(ret)
    ret = solution.lastRemaining1(param, param2)
    print(ret)
    ret = solution.lastRemaining2(param, param2)
    print(ret)

'''剑指 Offer 62. 圆圈中最后剩下的数字

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
