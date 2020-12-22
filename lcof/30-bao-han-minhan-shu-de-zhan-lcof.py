#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        #保存数据的栈
        self.stack = []
        #保存最小值的栈
        self.helper = []

    def push(self, x: int) -> None:
        if self.size == 0:
            self.stack.append(x)
            self.helper.append(x)
        else:
            if x < self.helper[self.size-1]:
                self.helper.append(x)
            else:
                self.helper.append(self.helper[self.size-1])
            self.stack.append(x)
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.helper.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size-1]

    def min(self) -> int:
        return self.helper[self.size-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)

    ret = obj.min()
    print(ret)
    obj.pop()

    ret = obj.top()
    print(ret)

    ret = obj.min()
    print(ret)

'''剑指 Offer 30. 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 

注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
