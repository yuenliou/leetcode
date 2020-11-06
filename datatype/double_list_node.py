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
        self.size = 0
        self.head = head
        self.tail = head

    def get(self, index: int):
        i = 0
        list_node = self.head
        while list_node and i < index:
            list_node = list_node.next
            i += 1
        if list_node: return list_node.val
        return -1

    def addAtHead(self, val: int):
        pass

    def addAtTail(self, val: int):
        pass

    def addAtIndex(self, index: int, val: int):
        pass

    def deleteAtIndex(self, index: int):
        pass

    def length(self) -> int:
        pass

    def clear(self):
        pass

def double_list_node_test():
    pass

if __name__ == '__main__':
    double_list_node_test()
