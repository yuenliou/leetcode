#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class TrieNode:
    def __init__(self, isEnd=False, next=None):
        """
        前缀树节点结构，特性：一次建树，多次查询

        这时字母映射表next 的妙用就体现了，TrieNode* next[26]中保存了对当前结点而言下一个可能出现的所有字符的链接，因此我们可以通过一个父结点来预知它所有子结点的值：
        https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/trie-tree-de-shi-xian-gua-he-chu-xue-zhe-by-huwt/

        python简单实现：哈希表
        https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/pythonjian-dan-shi-xian-by-powcai/
        """
        # 是否单词末尾
        self.isEnd = isEnd
        # 数组长度26
        self.next = [None] * 26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if not node.next[ord(c)-97]:
                node.next[ord(c)-97] = TrieNode()
            node = node.next[ord(c)-97]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if not node.next[ord(c)-97]:
                return False
            node = node.next[ord(c)-97]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if not node.next[ord(c)-97]:
                return False
            node = node.next[ord(c)-97]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    #初始化前缀树
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) # 返回 true
    print(trie.search("app")) # 返回 false
    print(trie.startsWith("app")) # 返回 true
    trie.insert("app")
    print(trie.search("app")) # 返回 true

'''208. 实现 Trie (前缀树)

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    main()
