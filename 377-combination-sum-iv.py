#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """穷举超时：vs 39. 组合总和"""
        def backtrack(start, track):
            #结束条件:sum >= target
            if sum(track) == target: return res.append(track[:])
            if sum(track) > target: return

            #顺序不同的序列被视作不同的组合：排列数问题，从0开始
            for i in range(start, len(nums)):
                # 做选择
                track.append(nums[i])
                # 进入下一行决策：包含当前元素
                backtrack(0, track)
                # 撤销选择
                track.pop()

        res = []
        backtrack(0, [])
        return len(res)

    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        """动态规划-状态转移方程：动态规划：自下而上
        dp[i] ：对于给定的由正整数组成且不存在重复数字的数组，和为 i 的组合的个数。
        状态转移方程：dp[i] = sum{dp[i - num] for num in nums and if i >= num}
        """
        #dp 数组的定义：当目标金额为 i 时，和为给定目标正整数的组合的个数。
        dp = [0] * (target+1)
        dp[0] = 1
        # 外层 for 循环 遍历状态
        for i in range(1, target + 1):
            # 内层 for 循环 遍历选择
            for num in nums:
                if i - num >= 0:
                    dp[i] = dp[i] + dp[i - num]
            # print(dp)
        print(dp)
        return dp[target]

    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        """动态规划：等价上面"""
        N = len(nums)
        W = target
        #dp定义
        dp = [0] * (W+1)
        #初始化
        dp[0] = 1
        #状态转移(两层循环：当前行第一列的初始状态)
        for i in range(1, W + 1):
            for j in range(1, N + 1):
                if i >= nums[j - 1]:
                    # print(i, j, i, j - nums[i - 1])
                    dp[i] = dp[i] + dp[i - nums[j - 1]]
            # print(dp)
        print(dp)
        return dp[W]

    def combinationSum4_3(self, nums: List[int], target: int) -> int:
        """动态规划-状态转移方程：动态规划：自下而上
        https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-python-dai-ma-by-liweiwei1419/
        说明：这个题是排列问题，从状态定义上就是一维的状态，所以无法用二维数组来表达，和518代码很像(518是状态压缩简化到一维)，但是有本质的区别
        """
        N = len(nums)
        W = target
        #dp 数组的定义：当目标金额为 i 时，和为给定目标正整数的组合的个数。
        dp = [[0] * (N + 1) for _ in range(W + 1)]
        #初始化-第一行
        for i in range(N + 1):
            dp[0][i] = 1

        #状态转移(两层循环：当前行第一列的初始状态)
        for i in range(1, W + 1):
            for j in range(1, N + 1):
                if i >= nums[j - 1]:
                    # print(i, j, i, j - nums[i - 1])
                    dp[i][j] = dp[i - 1][j] + dp[i][i - nums[j - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[W][N]

    def combinationSum4_4(self, nums: List[int], target: int) -> int:
        """两层循环优化:0-1背包状态压缩, vs 322 内外循环不能颠倒, 组合讲究顺序"""
        N = len(nums)
        W = target
        #dp定义
        dp = [0] * (W+1)
        #初始化
        dp[0] = 1
        #状态转移(两层循环：当前行第一列的初始状态)
        for i in range(1, N + 1):
            for j in range(nums[i - 1], W + 1):
                    # print(i, j, i, j - nums[i - 1])
                    dp[j] = dp[j] + dp[j - nums[i - 1]]
        # print(dp)
        return dp[W]

def main():
    param = [1, 2, 3]
    param2 = 4
    solution = Solution()
    ret = solution.combinationSum4(param, param2)
    print(ret)
    ret = solution.combinationSum4_1(param, param2)
    print(ret)
    ret = solution.combinationSum4_2(param, param2)
    print(ret)
    ret = solution.combinationSum4_3(param, param2)
    print(ret)
    ret = solution.combinationSum4_4(param, param2)
    print(ret)

'''377. 组合总和 Ⅳ

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

致谢：
特别感谢 @pbrother 添加此问题并创建所有测试用例。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
