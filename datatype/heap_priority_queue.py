#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# Definition for HeapPriorityQueue.

"""
https://www.cnblogs.com/kumata/p/9201571.html

堆(heap)
又被为优先队列(priority queue)。尽管名为优先队列，但堆并不是队列。回忆一下，在队列中，我们可以进行的限定操作是dequeue和enqueue。

dequeue是按照进入队列的先后顺序来取出元素。而在堆中，我们不是按照元素进入队列的先后顺序取出元素的，而是按照元素的优先级取出元素。

性质
堆的实现通过构造二叉堆（binary heap），实为二叉树的一种；由于其应用的普遍性，当不加限定时，均指该数据结构的这种实现。这种数据结构具有以下性质。

任意节点小于（或大于）它的所有后裔，最小元（或最大元）在堆的根上（堆序性）。
堆总是一棵完全树。即除了最底层，其他层的节点都被元素填满，且最底层尽可能地从左到右填入。
实现
堆的主要操作是插入和删除最小元素(元素值本身为优先级键值，小元素享有高优先级)
在插入或者删除操作之后，我们必须保持该实现应有的性质: 1. 完全二叉树 2. 每个节点值都小于或等于它的子节点

上浮（Promotion）
情境: 子节点的键值变为比父节点的键值大；如下面添加字节点
消除这种违反项：
交换子节点的键和父节点的键
重复这个过程直到堆的顺序恢复正常

下沉（Demotion）
情境：父节点的键值变得比子节点（一个或者2个） 的键值还小 ，如下面删除了根节点后拿了个小子节点补充上来的情况
消除这种违反项：
把父节点的键值和比它大的子节点的键值做交换
重复这个操作直到堆的顺序恢复正常
"""

# 该heap为min_heap，即根节点为最小值
class PriorityQueueBase:
    # 抽象基类为堆

    class Item:
        # 轻量级组合来存储堆项目
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):  # 比较大小
            return self._key < other._key

        def is_empty(self):
            return len(self) == 0

        def __str__(self):
            return str(self._key)


class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):  # 在后面加上然后加上
        self._data.append(self.Item(key, value))
        #添加到后面然后元素上浮
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        #交换元素，弹出后面，首元素下沉
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):  # 往上交换
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):  # 往下交换，递归比较三个值
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)


if __name__ == '__main__':
    """
    1. 常用的建堆方法主要用于堆元素已经确定(n/2...0)好的情况，而插入建堆的过程主要用于动态的增加元素来建堆。
    2. 插入建堆的过程也常用于建立优先队列的应用。这些可以根据具体的时间情况来选取。
    """
    heap = HeapPriorityQueue()
    heap.add(4, "D")
    heap.add(3, "C")
    heap.add(1, "A")
    heap.add(5, "E")
    heap.add(2, "B")
    heap.add(7, "G")
    heap.add(6, "F")
    heap.add(26, "Z")

    for item in heap._data:
        print(item)

    print("min is: ")
    print(heap.min())
    print()

    print("remove min: ")
    print(heap.remove_min())
    print("Now min is: ")
    print(heap.min())
    print()

    print("remove min: ")
    print(heap.remove_min())
    print("Now min is: ")
    print(heap.min())
    print()

    heap.add(1, "A")
    print("Now min is: ")
    print(heap.min())
    print()

    '''
    #输出结果
    1
    2
    3
    5
    4
    7
    6
    26
    min is: 
    (1, 'A')
    
    remove min: 
    (1, 'A')
    Now min is: 
    (2, 'B')
    
    remove min: 
    (2, 'B')
    Now min is: 
    (3, 'C')
    
    Now min is: 
    (1, 'A')
    '''
