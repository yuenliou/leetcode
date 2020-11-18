#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for double-linked list.
class DoubleListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyDoubleListNode:

    def __init__(self, size=0, head=None, tail=None):
        """size/tail简化某些操作"""
        self.size = 0
        self.head = head
        self.tail = head

    def get(self, index: int):
        i = 0
        node = self.head
        while node and i < index:
            node = node.next
            i += 1
        if node: return node.val
        return -1

    def addAtHead(self, val: int):
        if self.head:
            node = DoubleListNode(val)
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = DoubleListNode(val)
            self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int):
        if self.tail:
            node = DoubleListNode(val)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.tail = DoubleListNode(val)
            self.head = self.tail
        self.size += 1

    def addAtIndex(self, index: int, val: int):
        """三种情况0,size,0-size"""
        if index <= 0:
            return self.addAtHead(val)
        if index >= self.size:
            return self.addAtTail(val)

        p = None
        cur = self.head
        i = 0
        while cur and i < index:
            p = cur
            cur = cur.next
            i += 1
        node = DoubleListNode(val)
        node.prev = p
        node.next = cur
        p.next = node
        cur.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int):
        # 空链表
        if not self.head: return
        if index == 0:
            node = self.head
            self.head = self.head.next
            if self.head: # 链表有2个以上节点
                self.head.prev = None
            else: # 链表只有一个节点，将尾部置空
                self.tail = None
            del node
            self.size -= 1
            return

        if index == self.size - 1:
            node = self.tail
            self.tail = self.tail.prev
            if self.tail: # 注意这里不用处理tail为空，因为tail为空的话，那么链表只有单个节点。然而单个节点只能删除0号节点，只有index为0时才能删除，前面已经处理过了index为0的情况了，所以这里不在处理
                self.tail.next = None
            del node
            self.size -= 1
            return

        p = None
        cur = self.head
        i = 0
        while cur:
            if i == index:
                node = cur
                p.next=cur.next
                if cur.next:
                    cur.next.prev = p
                del node
                self.size -= 1
                return
            p = cur
            cur = cur.next
            i += 1

    def length(self) -> int:
        return self.size

    def clear(self):
        # self.size = 0
        # self.head = None
        # self.tail = None
        for i in range(self.size - 1, -1, -1):
            self.deleteAtIndex(i)

def double_node_test():
    my_list_node = MyDoubleListNode()

    my_list_node.addAtHead(1)
    my_list_node.addAtTail(3)
    my_list_node.addAtHead(4)
    my_list_node.addAtHead(5)
    my_list_node.addAtIndex(1, 2)

    print('length:', my_list_node.length())

    node = my_list_node.head
    while node:
        print(node.val)
        node = node.next

    my_list_node.deleteAtIndex(2)
    print('length:', my_list_node.length())

    node = my_list_node.tail
    while node:
        print(node.val)
        node = node.prev

    my_list_node.clear()
    print('length:', my_list_node.length())


if __name__ == '__main__':
    double_node_test()
