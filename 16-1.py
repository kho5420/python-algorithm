
# 208
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        self.trie[word] = word

    def search(self, word: str) -> bool:
        return self.trie.get(word)

    def startsWith(self, prefix: str) -> bool:
        for key in self.trie.keys():
            if self.trie[key][0:len(prefix)] == prefix:
                return True

        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)