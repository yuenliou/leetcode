#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def exchange(nums: List[int]) -> List[int]:
    length = len(nums)
    head, tail = 0, length-1
    while head < tail:
        #位运算判断奇偶
        while head < length-1 and nums[head] & 1 == 1:#偶数
            head += 1
        while tail > 0 and nums[tail] & 1 == 0:#奇数
            tail -= 1
        if head < tail:
            nums[head], nums[tail] = nums[tail], nums[head]
    return nums

def main():
    """
    思路1.从头开始迭代，找到一个偶数(i)挪到尾部，移动len-i个元素
    思路2.前后双指针，一遍遍历
    """
    param = [1, 3, 5]
    ret = exchange(param)
    print(ret)

'''剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
