#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def lengthOfLongestSubstring(s: str) -> int:
    """难道这是滑动窗口？？"""
    length = len(s)
    if length <= 0: return 0

    count = 1
    for i in range(length):
        for j in range(i+1, length):
            # print(i, j)
            if s[j] in s[i:j]:
                # print(i, j, s[i:j], '--')
                count = max(count, j-i)
                break
            if j == length - 1:
                count = max(count, j-i+1)
    return count

def lengthOfLongestSubstring1(s: str) -> int:
    """
    :type s: str
    :rtype: int
    说明：j 表示子串终止位置，i 表示字串起始位置 当未出现重复时，字符串的长度即为字符串的结束位置减去起始位置。
    发生重复时，重新利用字符串的结束位置j减去新的起始位置i，并与之前的未重复字串的长度作比较取较大者。
    PS：字典st记录字符出现的位置，两个相同字符之间的距离，就是无重复字符的长度
    ###奇淫技巧，不可复制，请关注下列滑动窗口###
    """
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            # i = st[s[j]] # "abba"
            i = max(st[s[j]], i)
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    return ans

def lengthOfLongestSubstring2(s: str) -> int:
    """滑动窗口+set"""
    length = len(s)
    if length <= 0: return 0

    # 哈希集合，记录每个字符是否出现过
    occ = set()

    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    j, count = -1, 0
    for i in range(length):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])

        while j + 1 < length and s[j + 1] not in occ:
            occ.add(s[j + 1])
            # 不断地移动右指针
            j += 1

        # 第 i 到 j 个字符是一个极长的无重复字符子串
        count = max(count, j-i+1)
    return count

def lengthOfLongestSubstring3(s: str) -> int:
    """滑动窗口+set"""
    if not s: return 0
    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    #区别于v2：外层循环代表的含义不一样，这里是右边界，v2是左边界
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:#abba窗口缩小
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len: max_len = cur_len
        lookup.add(s[i])
    return max_len

def lengthOfLongestSubstring4(s: str) -> int:
    """滑动窗口模板：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/"""
    if not s: return 0
    from collections import defaultdict
    lookup = defaultdict(int)
    start = 0
    end = 0
    max_len = 0
    counter = 0
    while end < len(s):
        if lookup[s[end]] > 0:
            counter += 1
        lookup[s[end]] += 1
        end += 1
        while counter > 0:
            if lookup[s[start]] > 1:
                counter -= 1
            lookup[s[start]] -= 1
            start += 1
        max_len = max(max_len, end - start)
    return max_len

def lengthOfLongestSubstring5(s: str) -> int:
    # 经典滑动窗口模板框架
    if not s: return 0
    from collections import defaultdict
    # 使用 window 作为计数器记录窗口中的字符出现次数
    window = defaultdict(int)
    left = right = 0
    res = 0
    # 增加窗口right
    while right < len(s):
        window[s[right]] += 1
        # 缩小窗口left
        while window[s[right]] > 1:
            window[s[left]] -= 1
            left += 1
        right += 1 # 放上面的，第二个 while 中需要 -1 处理
        res = max(res, right - left)
    return res

def main():
    param = "abcabcbb"
    # param = "bbbbb"
    # param = "pwwkew"
    # param = "au"
    # param = " "
    # param = "abba"
    ret = lengthOfLongestSubstring5(param)
    print(ret)

'''3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
