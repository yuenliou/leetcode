#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import queue
import collections

class MaxQueue:

    def __init__(self):
        #数据队列
        # self.queue = queue.Queue() #超时
        self.queue = []
        #辅助队列：deque 队首元素就是队列的最大值
        self.deque = collections.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.queue.append(value)
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        ans = self.queue.pop(0)
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

def main():
    obj = MaxQueue()
    obj.push_back(1)
    obj.push_back(2)
    ret = obj.max_value()
    print(ret)
    ret = obj.pop_front()
    print(ret)
    ret = obj.max_value()
    print(ret)

'''剑指 Offer 59 - II. 队列的最大值

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
