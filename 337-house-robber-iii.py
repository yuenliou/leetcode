#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from datatype.tree_node import TreeNode

class Solution:

    def rob(self, root: TreeNode) -> int:
        """
        动态规划：
        dp[node][j] ：这里 node 表示一个结点，以 node 为根结点的树，并且规定了 node 是否偷取能够获得的最大价值。
        j = 0 表示 node 结点不偷取；
        j = 1 表示 node 结点偷取。
        """

        def dfs(root):
            # (不抢root, 抢root)
            if not root: return (0, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            # dp[0]：以当前 node 为根结点的子树能够偷取的最大价值，规定 node 结点不偷
            # dp[1]：以当前 node 为根结点的子树能够偷取的最大价值，规定 node 结点偷

            #不抢root，抢子节点收益大的
            rob0 = max(left[0], left[1]) + max(right[0], right[1])
            #抢root，子节点不能抢
            rob1 = root.val + left[0] + right[0]
            return (rob0, rob1)

        return max(dfs(root))

def main():
    root = TreeNode(3)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    n5 = TreeNode(1)
    root.setLeftNode(n2)
    root.setRightNode(n3)
    n2.setRightNode(n4)
    n3.setRightNode(n5)

    solution = Solution()
    ret = solution.rob(root)
    print(ret)

'''337. 打家劫舍 III

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
