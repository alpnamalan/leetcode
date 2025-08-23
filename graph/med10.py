### AUG 21, 2025 -- P208: IMPLEMENT TRIE (PREFIX TREE) ###

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False # distinguish between a prefix and a full word.

class Trie:
    def __init__(self):
        self.root = TrieNode()   

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        
    def search(self, word: str) -> bool: 
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end # same prefix, not necessarily the same word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
