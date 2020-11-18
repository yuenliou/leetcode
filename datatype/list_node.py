#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for single-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyListNode:

    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        """
        获取链表指定节点的值，没有找到的话返回-1
        """
        i = 0
        list_node = self.head
        while list_node and i < index:
            list_node = list_node.next
            i += 1
        if list_node: return list_node.val
        return -1

    def addAtHead(self, val: int):
        """
        在链表头部插一个值为val的节点
        """
        head_node = ListNode(val)
        head_node.next = self.head
        self.head = head_node

    def addAtTail(self, val: int):
        """
        在链表尾部添加一个值为val的节点
        """
        tail_node = ListNode(val)
        if not self.head:
            self.head = tail_node #空链表直接赋值head
            return
        list_node = self.head
        while list_node.next:
            list_node = list_node.next
        if list_node:
            list_node.next = tail_node

    def addAtIndex(self, index: int, val: int):
        """
        在索引为index的节点之前添加值为val的节点
        """
        add_node = ListNode(val)
        if index <= 0:
            add_node.next = self.head
            self.head = add_node
            return
        i = 0
        list_node = self.head
        while list_node and i < index - 1: #插入删除需要找到前驱节点
            list_node = list_node.next
            i += 1
        if list_node:
            add_node.next = list_node.next
            list_node.next = add_node

    def deleteAtIndex(self, index: int):
        """
        删除索引为index的节点
        """
        if index == 0 and self.head:
            del_node = self.head
            self.head = self.head.next
            del del_node
            return
        i = 0
        list_node = self.head
        while list_node and i < index - 1:
            list_node = list_node.next
            i += 1
        if not list_node: return
        if list_node.next:
            del_node = list_node.next
            list_node.next = del_node.next
            del del_node

    def length(self) -> int:
        """
        链表长度
        :return:
        """
        len = 0
        list_node = self.head
        while list_node:
            len += 1
            list_node = list_node.next
        return len

    def clear(self):
        """
        清空链表
        """
        # self.head = None
        del_node = None
        while self.head:
            del_node = self.head
            self.head = self.head.next
            del del_node

def list_node_test():
    my_list_node = MyListNode()

    my_list_node.addAtTail(5)
    my_list_node.addAtHead(1)
    my_list_node.addAtIndex(0, 10)
    my_list_node.addAtIndex(1, 20)
    my_list_node.addAtIndex(2, 30)
    my_list_node.addAtIndex(3, 40)
    my_list_node.addAtTail(50)
    my_list_node.addAtTail(60)

    node = my_list_node.head
    while node:
        print(node.val)
        node = node.next

    my_list_node.deleteAtIndex(2)

    print('length:', my_list_node.length())

    for i in range(my_list_node.length()):
        print(my_list_node.get(i))

    my_list_node.clear()
    print('length:', my_list_node.length())

if __name__ == '__main__':
    list_node_test()
