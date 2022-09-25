from re import L


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word : str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()

            curr = curr.children[c]
        
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            if c in curr.children:
                curr = curr.children[c]

            else:
                return False

        return curr.isWord


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]

            else:
                return False

        return True

if __name__ == '__main__':
    myTrie = Trie()

    testArray = ["Tree"]

    for x in testArray:
        myTrie.insert(x)