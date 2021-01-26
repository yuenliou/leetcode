#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List
from datatype.tree_node import TreeNode, pre_order_travel, in_order_travel, post_order_travel, level_order_travel

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        #广度有限遍历bfs
        if not root: return []
        queue = []
        queue.append(root)
        res = []
        while len(queue):
            #不要求"每一层打印到一行"，内层循环可以去掉，参考 题32-ii
            size = len(queue)
            while size > 0:
                #左出右进
                node = queue.pop(0)
                res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
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


'''剑指 Offer 32 - I. 从上到下打印二叉树

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
