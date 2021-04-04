# Creation
# O(n^2) time | O(n^2) space

# Searching
# O(n) time | O(1) space

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertStringInTrie(i, string[i:])

    def insertStringInTrie(self, index, string):
        node = self.root
        for s in string:
            if s not in node:
                node[s] = {}
            node = node[s]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for s in string:
            if s not in node:
                return False
            node = node[s]
        return self.endSymbol in node
