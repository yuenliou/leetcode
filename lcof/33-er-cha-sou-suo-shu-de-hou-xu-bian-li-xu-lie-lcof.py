#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """剑指Offer：判断有点繁琐"""
        length = len(postorder)
        if length <= 0: return True

        root = postorder[length - 1]
        #左子树小于跟节点，已经保证
        lIndex = 0
        for i in range(length - 1):
            if postorder[i] > root:
                break
            lIndex += 1

        #右子树大于跟节点，待求证
        rIndex = 0
        for i in range(lIndex, length - 1):
            if postorder[i] < root:
                return False
            rIndex += 1

        left = True
        if lIndex: left = self.verifyPostorder(postorder[:lIndex])
        right = True
        if rIndex: right = self.verifyPostorder(postorder[lIndex:lIndex+rIndex])

        return left and right

    def verifyPostorder1(self, postorder: List[int]) -> bool:
        """递归分治：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/"""
        def recur(i, j):
            #终止条件： 当 i >= j ，说明此子树节点数量 <=1，无需判别正确性，因此直接返回 true
            if i >= j: return True
            #计数判断
            p = i
            while postorder[p] < postorder[j]: p += 1 #先定左区间，小于root
            m = p
            while postorder[p] > postorder[j]: p += 1 #判断右区间，是否都大于
            # 左子树区间 [i, m - 1]、右子树区间 [m, j - 1]、根节点索引 j
            return p == j and recur(i, m - 1) and recur(m, j - 1)
        return recur(0, len(postorder) - 1)

def main():
    param = [1,6,3,2,5]
    param = [1,3,2,6,5]
    solution = Solution()
    ret = solution.verifyPostorder(param)
    print(ret)
    ret = solution.verifyPostorder1(param)
    print(ret)

'''剑指 Offer 33. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
