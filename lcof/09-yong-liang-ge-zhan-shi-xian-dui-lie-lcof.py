#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class CQueue:

    def __init__(self):
        #保存数据的栈：插入栈
        self.stack = []
        #辅助功能栈：删除栈，pop的时候：如果有元素直接弹出，没有元素的话从数据栈拿
        self.helper = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if len(self.helper) == 0 and len(self.stack) == 0:
            return -1
        if len(self.helper) == 0:
            while len(self.stack):
                self.helper.append(self.stack.pop())
        return self.helper.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

def main():
    obj = CQueue()
    obj.appendTail(3)
    ret = obj.deleteHead()
    print(ret)
    ret = obj.deleteHead()
    print(ret)

'''剑指 Offer 09. 用两个栈实现队列

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
