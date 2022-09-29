class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.searchNum = 0

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.isWord = True
        curr.searchNum += 1

    def search(self, word):
        curr = self.head

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return curr.isWord

    def prefix(self, prefix):
        curr = self.head

        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return True

    def searchPossibleWords(self, prefix):
        word = ""

        curr = self.head

        for c in prefix:
            if c not in curr.children:
                return False

            word += c
            curr = curr.children[c]

        possibleWords = []

        def bfs(node, currWord = word):
            print(len(node.children))
            if len(node.children) == 0:
                possibleWords.append([node.searchNum, currWord])
                return  
            
            for x in node.children:
                bfs(node.children[x], currWord + x)

        bfs(curr)

        print(possibleWords)
        

if __name__ == "__main__":
    testTrie = Trie()
    testArray = ["apple", "arrow", "appalachian", "temporary", "temperature", "augment", "apple"]

    for x in testArray:
        testTrie.insert(x)

    print(testTrie.head.children)


    testTrie.searchPossibleWords("ap")

