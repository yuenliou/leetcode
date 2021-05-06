#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:
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
        res = []
        # 增加窗口right
        while right < len(s):
            # 维护counter1
            if window[s[right]] > 0:
                counter -= 1
            window[s[right]] -= 1
            right += 1
            # 缩小窗口left
            while counter == 0:
                if right - left == len(t):
                    res.append(left)
                # 维护counter2
                if window[s[left]] == 0:
                    counter += 1
                window[s[left]] += 1
                left += 1
        return res

    def findAnagrams2(self, s: str, t: str) -> List[int]:
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
        res = []
        # 增加窗口right
        while right < len(s):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    counter += 1
            right += 1
            # 缩小窗口left
            while counter == len(need):
                if right - left == len(t):
                    res.append(left)

                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        counter -= 1
                left += 1
        return res

def main():
    param = "cbaebabacd"
    param2 = "abc"
    solution = Solution()
    ret = solution.findAnagrams(param, param2)
    print(ret)
    ret = solution.findAnagrams2(param, param2)
    print(ret)

'''438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
