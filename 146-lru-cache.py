#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from collections import OrderedDict

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """官方实现"""
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            print(-1)
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        print(node.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        print(self.cache.keys())

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

class LinkedListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        # return f'{self.key} : {self.val}'
        # return '{}:{}'.format(self.key, self.val)
        return "{%s:%s}" % (self.key, self.val)

class LRUCache4():
    def __init__(self, capacity: int):
        # 没有哑结点的实现
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            value = node.val
            self.removeNode(node)
            self.addToHead(node)
        else:
            value = -1
        print(value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.val = value
            # move to head
            self.removeNode(node)
            self.addToHead(node)
        else:
            node = LinkedListNode(key, value)
            self.cache.update({key:node})
            self.addToHead(node)
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
        print(self.cache.keys())

    def addToHead(self, node):
        # 清空prev/next
        node.prev = None
        node.next = None
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = self.head
        self.size += 1

    def removeNode(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1

    def removeNode_(self, node):
        """上述的详版"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        del node
        self.size -= 1

    def removeNode2(self, node):
        if node.prev:
            #next分支
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                node.prev.next = None
                self.tail = node.prev
        else:
            #next分支
            if node.next:
                node.next.prev = None
                self.head = node.next
            else:
                self.head = None
                self.tail = None
        self.size -= 1

    def removeNode3(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            # node.next.prev = None
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            # node.prev.next = None
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

    def removeTail(self) -> LinkedListNode:
        node = self.tail
        # self.removeNode(node)
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        return node


class LRUCache3(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            print(-1)
            return -1
        self.move_to_end(key)
        print(self[key])
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
            # oldest = next(iter(self))
            # del self[oldest]
        print(self)

class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # cache可以不用(见LRUCache3)，直接用orderedDict中的dict
        self.cache = {}
        # 这里只用了OrderedDict中的双链表
        self.orderedDict = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if not value:
            return -1
        self.orderedDict.move_to_end(key)
        print(value)
        return value

    def put(self, key: int, value: int) -> None:
        self.cache.update({key:value})
        self.orderedDict.update({key:value})
        self.orderedDict.move_to_end(key)
        if len(self.orderedDict) > self.capacity:
            pop = self.orderedDict.popitem(last=False)
            #需要删除cache中对应的key
            self.cache.pop(pop[0])
        print(self.cache)
        print(self.orderedDict)

class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashTable = {}
        #根据时间戳实现的一个排序字典orderDict（有序映射linkedHashMap），这玩意也可以叫字典+双向队列
        self.weightTable = {}

    def get(self, key: int) -> int:
        import time
        value = self.hashTable.get(key, -1)
        if value != -1:
            self.weightTable.update({key: int(time.time() * 1000 ** 2)})
        print(value)
        return value

    def put(self, key: int, value: int) -> None:
        import time
        self.weightTable.update({key:int(time.time() * 1000**2)})

        self.hashTable.update({key:value})
        weightTuple = sorted(self.weightTable.items(), key=lambda e:e[1], reverse=True)
        # print(weightTuple)
        i = 0
        for k, v in weightTuple:
            # print('k=', k, 'v=', v)
            i += 1
            if i > self.capacity:
                self.weightTable.pop(k)
                self.hashTable.pop(k)
        print(self.hashTable)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    lRUCache = LRUCache2(2)
    lRUCache.put(1, 1) # 缓存是 {1 = 1}
    lRUCache.put(2, 2) # 缓存是 {1 = 1, 2 = 2}
    lRUCache.get(1) # 返回 1
    lRUCache.put(3, 3) # 该操作会使得关键字 2 作废，缓存是 {1 = 1, 3 = 3}
    lRUCache.get(2) # 返回 - 1(未找到)
    lRUCache.put(4, 4) # 该操作会使得关键字 1 作废，缓存是 {4 = 4, 3 = 3}
    lRUCache.get(1) # 返回 - 1(未找到)
    lRUCache.get(3) # 返回 3
    lRUCache.get(4) # 返回 4

'''146. LRU缓存机制

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
