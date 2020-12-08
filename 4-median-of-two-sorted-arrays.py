#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    官方解法一：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
    精选解法三：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
    评论区：为了简化代码，不分情况讨论，我们使用一个小trick，我们分别找第 (m+n+1) / 2 个，和 (m+n+2) / 2 个，然后求其平均值即可，这对奇偶数均适用。假入 m+n 为奇数的话，那么其实 (m+n+1) / 2 和 (m+n+2) / 2 的值相等，相当于两个相同的数字相加再除以2，还是其本身。
    """
    def getKth(nums1, start1, end1, nums2, start2, end2, k) -> int:
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1
        if len1 > len2: return getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0: return nums2[start2 + k - 1]

        if k == 1: return min(nums1[start1], nums2[start2])

        # 数组长度小于 k/2 情况
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        """评论区：【最佳入手BEGINING】
        //i: nums1的起始位置 j: nums2的起始位置
        public int findKth(int[] nums1, int i, int[] nums2, int j, int k){
            if( i >= nums1.length) return nums2[j + k - 1];//nums1为空数组
            if( j >= nums2.length) return nums1[i + k - 1];//nums2为空数组
            if(k == 1){
                return Math.min(nums1[i], nums2[j]);
            }
            int midVal1 = (i + k / 2 - 1 < nums1.length) ? nums1[i + k / 2 - 1] : Integer.MAX_VALUE;
            int midVal2 = (j + k / 2 - 1 < nums2.length) ? nums2[j + k / 2 - 1] : Integer.MAX_VALUE;
            if(midVal1 < midVal2){
                return findKth(nums1, i + k / 2, nums2, j , k - k / 2);
            }else{
                return findKth(nums1, i, nums2, j + k / 2 , k - k / 2);
            }        
        }
        """
        if nums1[i] > nums2[j]:
            return getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))

    n, m = len(nums1), len(nums2)
    left = (n + m + 1) // 2
    right = (n + m + 2) // 2
    return (getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2

def main():
    param = [1,2]
    param2 = [3,4]
    ret = findMedianSortedArrays(param, param2)
    print(ret)

'''4. 寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
