#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel, level_order_travel

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #广度有限遍历bfs，"之"字遍历
        if not root: return []
        queue = []
        queue.append(root)
        res = []
        reverse = False #False奇数层，True偶数层。
        while len(queue):
            reverse = not reverse
            size = len(queue)
            tmp = []
            while size > 0:
                #左出右进
                node = queue.pop(0)
                #遍历顺序没变呀！对结果数组逆序了
                tmp.append(node.val) if reverse else tmp.insert(0, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
            res.append(tmp)
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        #广度有限遍历bfs，"之"字遍历，双端队列&双栈
        if not root: return []
        queue = []
        queue.append(root)
        res = []
        reverse = False #False奇数层，True偶数层。
        while len(queue):
            reverse = not reverse

            #奇数层
            size = len(queue)
            tmp = []
            while size > 0:
                #左出右进
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
            res.append(tmp)

            if not queue: break # 若为空则提前跳出

            # 偶数层
            size = len(queue)
            tmp = []
            while size > 0:
                # 右出左进
                node = queue.pop()
                tmp.append(node.val)
                if node.right: queue.insert(0, node.right)
                if node.left: queue.insert(0, node.left)
                size -= 1
            res.append(tmp)
        return res

def main():
    root = TreeNode(1)
    rLeft = TreeNode(2)
    rRight = TreeNode(3)

    root.setLeftNode(rLeft)
    root.setRightNode(rRight)

    rLeft.setLeftNode(TreeNode(4))
    rRight.setRightNode(TreeNode(5))

    print('-level-')
    level_order_travel(root)

    solution = Solution()
    ret = solution.levelOrder(root)
    print(ret)
    ret = solution.levelOrder1(root)
    print(ret)


'''剑指 Offer 32 - III. 从上到下打印二叉树 III

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
