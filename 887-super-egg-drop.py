#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """动态规划：dp(K, N)就是当前拥有的鸡蛋数K和需要测试的楼层数N
        labuladong:https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484675&idx=1&sn=4a4ac1c0f1279530b42fedacc6cca6e6&chksm=9bd7fb0baca0721dda1eaa1d00b9a520672dc9d5c3be762eeca869be35d7ce232922ba8e928b&scene=21#wechat_redirect
        """
        memo = dict()

        def dp(K, N) -> int:
            # base case
            if K == 1: return N
            if N == 0: return 0
            # 避免重复计算
            if (K, N) in memo: return memo[(K, N)]

            res = float('INF')
            # 穷举所有可能的选择，每层循环都是一个选择
            for i in range(1, N + 1):
                #鸡蛋碎了dp(K - 1, i - 1)
                #鸡蛋没碎碎dp(K, N - i)
                res = min(res,
                          max(
                              dp(K, N - i),
                              dp(K - 1, i - 1)
                          ) + 1
                          )
            # 记入备忘录
            memo[(K, N)] = res
            return res

        return dp(K, N)

    def superEggDrop1(self, K: int, N: int) -> int:
        """
        动态规划：自下而上的迭代需要三个循环for
        作者：liweiwei1419
        链接：https:#leetcode-cn.com/problems/super-egg-drop/solution/dong-tai-gui-hua-zhi-jie-shi-guan-fang-ti-jie-fang/
        """
        # dp[i][j]：一共有 i 层楼梯的情况下，使用 j 个鸡蛋的最少实验的次数
        # 注意：
        # 1、i 表示的是楼层的大小，不是第几层的意思，例如楼层区间 [8, 9, 10] 的大小为 3，这一点是在状态转移的过程中调整的定义
        # 2、j 表示可以使用的鸡蛋的个数，它是约束条件，我个人习惯放在后面的维度，表示消除后效性的意思

        # 0 个楼层和 0 个鸡蛋的情况都需要算上去，虽然没有实际的意义，但是作为递推的起点，被其它状态值所参考
        # 由于求的是最小值，因此初始化的时候赋值为一个较大的数，9999 或者 i 都可以
        dp = [[float('inf')] * (K + 1) for _ in range(N + 1) ]

        # 初始化：填写下标为 0、1 的行和下标为 0、1 的列
        # 第 0 行：楼层为 0 的时候，不管鸡蛋个数多少，都测试不出鸡蛋的 F 值，故全为 0
        for j in range(K + 1):
            dp[0][j] = 0

        # 第 1 行：楼层为 1 的时候，0 个鸡蛋的时候，扔 0 次，1 个以及 1 个鸡蛋以上只需要扔 1 次
        dp[1][0] = 0
        for j in range(K + 1):
            dp[1][j] = 1

        # 第 0 列：鸡蛋个数为 0 的时候，不管楼层为多少，也测试不出鸡蛋的 F 值，故全为 0
        # 第 1 列：鸡蛋个数为 1 的时候，这是一种极端情况，要试出 F 值，最少次数就等于楼层高度（想想复杂度的定义）
        for i in range(N + 1):
            dp[i][0] = 0
            dp[i][1] = i

        # 从第 2 行，第 2 列开始填表
        for i in range(2, N + 1):
            for j in range(2, K + 1):
                for k in range(1, i + 1):
                    # 碎了，就需要往低层继续扔：层数少 1 ，鸡蛋也少 1
                    # 不碎，就需要往高层继续扔：层数是当前层到最高层的距离差，鸡蛋数量不少
                    # 两种情况都做了一次尝试，所以加 1
                    dp[i][j] = min(dp[i][j], max(dp[k - 1][j - 1], dp[i - k][j]) + 1)
        return dp[N][K]

    def superEggDrop2(self, K: int, N: int) -> int:
        """
        动态规划自下而上的迭代优化：二分优化
        """
        # dp[i][j]：一共有 i 层楼梯的情况下，使用 j 个鸡蛋的最少仍的次数
        dp = [[float('inf')] * (K + 1) for _ in range(N + 1) ]

        # 初始化：填写下标为 0、1 的行和下标为 0、1 的列
        # 第 0 行：楼层为 0 的时候，不管鸡蛋个数多少，都测试不出鸡蛋的 F 值，故全为 0
        for j in range(K + 1):
            dp[0][j] = 0

        # 第 1 行：楼层为 1 的时候，0 个鸡蛋的时候，扔 0 次，1 个以及 1 个鸡蛋以上只需要扔 1 次
        dp[1][0] = 0
        for j in range(K + 1):
            dp[1][j] = 1

        # 第 0 列：鸡蛋个数为 0 的时候，不管楼层为多少，也测试不出鸡蛋的 F 值，故全为 0
        # 第 1 列：鸡蛋个数为 1 的时候，这是一种极端情况，要试出 F 值，最少次数就等于楼层高度（想想复杂度的定义）
        for i in range(N + 1):
            dp[i][0] = 0
            dp[i][1] = i

        # 从第 2 行，第 2 列开始填表
        for i in range(2, N + 1):
            for j in range(2, K + 1):
                left, right = 1, i
                while left < right:
                    # 找 dp[k - 1][j - 1] <= dp[i - mid][j] 的最大值 k
                    mid = left + (right - left + 1) // 2
                    breakCount = dp[mid - 1][j - 1]
                    notBreakCount = dp[i - mid][j]

                    if breakCount > notBreakCount:
                    # 排除法（减治思想）写对二分见第 35 题，先想什么时候不是解
                    # 严格大于的时候一定不是解，此时 mid 一定不是解
                    # 下一轮搜索区间是[left, mid - 1]
                        right = mid - 1
                    else:
                        # 这个区间一定是上一个区间的反面，即[mid, right]
                        # 注意这个时候取中间数要上取整，int mid = left + (right - left + 1) / 2;
                        left = mid
                # left 这个下标就是最优的 k 值，把它代入转移方程 Math.max(dp[k - 1][j - 1], dp[i - k][j]) + 1) 即可
                dp[i][j] = max(dp[left - 1][j - 1], dp[i - left][j]) + 1
        return dp[N][K]


def main():
    param = 3
    param2 = 14
    solution = Solution()
    ret = solution.superEggDrop(param, param2)
    print(ret)
    ret = solution.superEggDrop1(param, param2)
    print(ret)
    ret = solution.superEggDrop2(param, param2)
    print(ret)

'''887. 鸡蛋掉落

你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

 

示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
示例 3：

输入：K = 3, N = 14
输出：4
 

提示：

1 <= K <= 100
1 <= N <= 10000

来源：力扣（LeetCode）
链接：https:#leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
