class TrieNode():
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.terminus = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        current = self.root

        for ch in word:
            if current.children.get(ch) == None:
                current.children[ch] = TrieNode(ch)
            current = current.children[ch]
        current.terminus = True

    def search(self, word:str):
        current = self.root

        for ch in word:
            if current.children.get(ch) == None:
                return False
            current = current.children[ch]
        return current.terminus

collection = Trie()
