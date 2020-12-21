#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """k 限制了树的高度，n 限制了树的宽度。
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485007&idx=1&sn=ceb42ba2f341af34953d158358c61f7c&chksm=9bd7f847aca071517fe0889d2679ead78b40caf6978ebc1d3d8355d6693acc7ec3aca60823f0&scene=21#wechat_redirect
        """
        def backtrack(start, track):
            #结束条件:到大树的底部
            if len(track) == k:
                return res.append(track[:])

            for i in range(start, n + 1):
                # 做选择
                track.append(i)
                # 进入下一行决策
                backtrack(i + 1, track)
                # 撤销选择
                track.pop()

        res = []
        if n <= 0 or k <= 0: return []
        backtrack(1, [])
        return res

def main():
    param = 4
    param2 = 2
    solution = Solution()
    ret = solution.combine(param, param2)
    print(ret)

'''77. 组合

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
