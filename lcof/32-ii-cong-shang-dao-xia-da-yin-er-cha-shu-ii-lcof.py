#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel, level_order_travel

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #广度有限遍历bfs
        if not root: return []
        queue = []
        queue.append(root)
        res = []
        while len(queue):
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
        return res

def main():
    root = TreeNode(3)
    rLeft = TreeNode(4)
    rRight = TreeNode(5)

    root.setLeftNode(rLeft)
    root.setRightNode(rRight)

    rLeft.setLeftNode(TreeNode(1))
    rLeft.setRightNode(TreeNode(2))

    solution = Solution()
    ret = solution.levelOrder(root)
    print(ret)
    print('-level-')
    level_order_travel(root)


'''剑指 Offer 32 - II. 从上到下打印二叉树 II

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

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
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
