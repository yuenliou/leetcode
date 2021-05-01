#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List


class Skiplist:

    def __init__(self):
        pass

    def search(self, target: int) -> bool:
        pass

    def add(self, num: int) -> None:
        pass

    def erase(self, num: int) -> bool:
        pass

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

def main():
    # 其实，知道与践行之间隔着巨大的鸿沟，知道那么多的算法，可是仍写不出牛逼的代码。
    # 还是要多写多练，不然就会被说 talk is cheap,show me the code。
    # 编码之前，应该思考一下跳表应支持的功能：
    # 1、插入一个元素 2、删除一个元素 3、查找一个元素 4、查找一个区间的元素 5、输出有序序列
    # ps1:插入时动态维护索引->随机算法(概率p为常数)，删除时索引层找到节点down删除(right)
    # ps2:跳表的期望空间复杂度为O(n)，跳表的查询，插入和删除操作的期望时间复杂度都为O(logn)

    skiplist = Skiplist()

    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    skiplist.search(0) # 返回 false
    skiplist.add(4)
    skiplist.search(1) # 返回 true
    skiplist.erase(0) # 返回 false，0 不在跳表中
    skiplist.erase(1) # 返回 true
    skiplist.search(1) # 返回 false，1 已被擦除

    # print(ret)

'''1206. 设计跳表

不使用任何库函数，设计一个跳表。

跳表是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 [30, 40, 50, 60, 70, 90]，然后增加 80、45 到跳表中，以下图的方式操作：


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

在本题中，你的设计应该要包含这些函数：

bool search(int target) : 返回target是否存在于跳表中。
void add(int num): 插入一个元素到跳表。
bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
了解更多 : https://en.wikipedia.org/wiki/Skip_list

注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

样例:

Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
约束条件:

0 <= num, target <= 20000
最多调用 50000 次 search, add, 以及 erase操作。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-skiplist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
