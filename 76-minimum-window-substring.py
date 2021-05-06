#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """滑动窗口模板：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/"""
        if not s or not t: return ''
        from collections import defaultdict
        # 使用 window 作为计数器记录窗口中的字符出现次数
        window = defaultdict(int)
        # init window
        for c in t: window[c] += 1
        # 维护 window 中符合元素的计数 counter
        counter = len(t)
        left = right = 0
        res_left, res_right = 0, float('inf')
        # 增加窗口right
        while right < len(s):
            # 维护counter1
            if window[s[right]] > 0:
                counter -= 1
            window[s[right]] -= 1
            right += 1
            # 缩小窗口left
            while counter == 0:
                if right - left < res_right - res_left:
                    res_left, res_right = left, right
                # 维护counter2
                if window[s[left]] == 0:
                    counter += 1
                window[s[left]] += 1
                left += 1
        # if res_right == float('inf'): res_right = res_left
        return '' if res_right == float('inf') else s[res_left:res_right]

    def minWindow2(self, s: str, t: str) -> str:
        # 滑动窗口 https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484504&idx=1&sn=5ecbab87e42033cc0a62b635cc436977&chksm=9bd7fa50aca07346a3ffa6be6fccc445968c162af9532fa9c6304eaab2e3a1b79a4bbe758c0a&scene=21#wechat_redirect
        if not s or not t: return ''
        from collections import defaultdict
        # 使用 window 作为计数器记录窗口中的字符出现次数
        window = defaultdict(int)
        # 两个哈希表当作计数器,对比window和need中的字符
        need = defaultdict(int)
        for c in t: need[c] += 1
        # 计数 counter
        counter = 0
        left = right = 0
        res_left, res_right = 0, float('inf')
        # 增加窗口right
        while right < len(s):
            if need[s[right]]:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    counter += 1
            right += 1
            # 缩小窗口left
            while counter == len(t):
                if right - left < res_right - res_left:
                    res_left, res_right = left, right

                if need[s[left]]:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        counter -= 1
                left += 1
        return '' if res_right == float('inf') else s[res_left:res_right]

def main():
    param = "ADOBECODEBANC"
    param2 = "ABC"
    solution = Solution()
    ret = solution.minWindow(param, param2)
    print(ret)
    ret = solution.minWindow2(param, param2)
    print(ret)

'''76. 最小覆盖子串

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
