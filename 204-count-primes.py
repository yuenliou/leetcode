#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def countPrimes(n: int) -> int:
    """暴力法超时：自然试除法2-log2N"""
    cnt = 0
    # c = 0
    for i in range(2, n): #2-n的所有数
        if i != 2 and i & 1 == 0: continue #优化1：合数直接过
        flag = False
        for j in range(2, i): #不包含1和本身
            if j ** 2 > i: break #优化1：2-log2N,
            # c += 1;print(c)# n = 100, 优化过程：提升效率(次数)1133/260/187
            if i % j == 0:
                flag = True
                break
        if not flag:
            # print(i)
            cnt += 1
    return cnt

def countPrimes1(n: int) -> int:
    """暴力法优化：自然试除法2-log2N"""
    cnt = 1 if n > 2 else 0
    # c = 0
    for i in range(3, n):  # 3-n的所有数
        if i != 2 and i & 1 == 0: continue  # 优化1：合数直接过

        flag = False
        # 不包含1和本身
        for j in range(3, i, 2):  # 优化3：i += 2
            if j ** 2 > i: break  # 优化1：2-log2N,
            # c += 1;print(c)  # n = 100, 优化过程：提升效率(次数)1133/260/187/87
            if i % j == 0:
                flag = True
                break
        if not flag:
            # print(i)
            cnt += 1
    return cnt

def countPrimes2(n: int) -> int:
    """厄拉多塞筛法：声明一个长度为最大限制数的布尔数组。用布尔值来区别筛选出的数和质数。"""
    cnt = 0
    flags = [0] * n
    for i in range(2, n):
        if not flags[i]:
            cnt += 1
            # 如果我们在进行顺序遍历时，每取得一个数（排除0、1），如果将它所有的倍数（排除0、1、本身）都清除，那么，剩下的数是不是必为素数？
            for j in range(i + i, n, i):
                #排除不是质数的数
                flags[j] = 1
    return cnt

def main():
    # 如何编程判断一个数是否是质数？
    # https://www.zhihu.com/question/308322307/answer/574767625
    param = 100
    ret = countPrimes2(param)
    print(ret)

'''204. 计数质数

统计所有小于非负整数 n 的质数的数量。

 

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0
 

提示：

0 <= n <= 5 * 106


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
