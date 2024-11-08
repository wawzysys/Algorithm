class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class PersistentTrie:
    def __init__(self):
        self.roots = [TrieNode()]  # 记录每个版本的根节点

    def insert(self, root_index, word):
        root = self.roots[root_index]
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        return len(word)

    def query(self, root_index, word):
        root = self.roots[root_index]
        node = root
        length = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            length += 1
        return length

    def modify(self, root_index, word, new_char):
        root = self.roots[root_index]
        node = root
        old_lengths = [0] * (len(word) + 1)
        new_lengths = [0] * (len(word) + 1)

        # 记录修改前每个节点的count
        for i, char in enumerate(word):
            old_lengths[i + 1] = node.count
            if char not in node.children:
                break
            node = node.children[char]

        # 修改节点并更新count
        node = root
        for i, char in enumerate(word):
            new_lengths[i + 1] = node.count
            if char not in node.children:
                break
            node = node.children[char]

        # 在修改处增加新字符
        node = root
        for i, char in enumerate(word):
            if char not in node.children:
                break
            node = node.children[char]
            node.count += 1
        node.children[new_char] = TrieNode()
        node = node.children[new_char]
        node.count += 1

        # 更新修改后的每个节点的count
        for i, count in enumerate(new_lengths):
            node.count = count - (old_lengths[i] if i < len(old_lengths) else 0)
            if i < len(word):
                char = word[i]
                if char not in node.children:
                    break
                node = node.children[char]

def calculate_prefix_score(trie, words):
    n = len(words)
    total_score = 0
    for i in range(n):
        for j in range(i + 1, n):
            prefix_length = trie.query(-1, words[i])  # 查询两个字符串的最长公共前缀长度
            total_score += prefix_length
    return total_score

def maximize_prefix_score(n, words):
    trie = PersistentTrie()
    score = 0

    # 初始构建trie
    for i, word in enumerate(words):
        score += trie.insert(-1, word)

    max_score = score
    for i in range(n):
        word = words[i]
        for j in range(len(word)):
            old_char = word[j]
            for new_char in range(ord('a'), ord('z') + 1):
                if new_char != ord(old_char):
                    new_word = word[:j] + chr(new_char) + word[j + 1:]
                    old_score = trie.query(-1, word)
                    new_score = trie.query(-1, new_word)
                    diff = new_score - old_score
                    if diff > 0:
                        trie.modify(-1, word, chr(new_char))
                        score += diff
                        max_score = max(max_score, score)
                    else:
                        trie.query(-1, word)  # 恢复状态

    return max_score

# 读取输入
n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

# 输出答案
print(maximize_prefix_score(n, words))
