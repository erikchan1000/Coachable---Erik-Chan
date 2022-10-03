class Node:
    def __init__(self, url, next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = self.head
        self.size = 0

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.searchNum = 0
        self.prefixUrls = []

class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.characterHashMap = {}
        
         
        # keys -> characters
        #values -> set in urls that contain the key

    def insert(self, word):
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr.children[c].prefixUrls.insertSorted(word)
            self.characterHashMap[c].append(word)
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

        return curr.prefixUrls

    def substringSearch(self, substring):
        curr = self.head

        for x in substring:
            


class BrowserHistory:
    def __init__(self):
        self.websites = DoublyLinkedList()
        self.currentPage = None
        self.hmap = {}
        self.currentIndex = 0
        self.stringTrie = Trie()
        self.possibleUrls = []

        

    def current_page(self):
        return self.currentPage

    def go_to(self, page):
        self.stringTrie.insert(page)
        
        if self.currentPage and self.currentPage.next is not None:
            self.currentPage.next = None


        if self.currentPage is None:
            self.currentPage = Node(page)

        else:

            myNode = Node(page)
            
            self.currentPage.next = myNode

            myNode.prev = self.currentPage

            self.currentPage = self.currentPage.next

        self.hmap[self.currentIndex] = self.currentPage
        self.currentIndex += 1

        print(self.currentPage.url)

    def go_back(self):

        if self.currentPage and self.currentPage.prev:
            self.currentPage = self.currentPage.prev
            self.currentIndex -= 1
            print(self.currentPage.url)

        else:
            return None

    def go_forward(self):
        if self.currentPage and self.currentPage.next:
            self.currentPage = self.currentPage.next
            print(self.currentPage.url)

        else:
            return None
            

    def skip_backward(self, N):
        endIndex = 0 if self.currentIndex - N < 0 else self.currentIndex - N
        
        self.currentIndex = self.hmap[endIndex]
        
    def skip_forward(self, N):
        endIndex = self.currentIndex + N
        
        if endIndex not in self.hmap:
            self.currentIndex = max(self.hmap)

        else:
            self.currentIndex = endIndex

        self.currentPage = self.hmap[self.currentIndex]

    def autocomplete(self, prefix, length = None):
        
        possibleUrls = self.stringTrie.searchPossibleWords(prefix)

        possibleUrls = [x[1] for x in possibleUrls]

        if not length or length >= len(possibleUrls):
            print(possibleUrls)

        else:
            print(possibleUrls[0 : length])

    def deleteHistory(self):
        pass



test = BrowserHistory()

test.go_to("test.com")

test.go_to("google.com")

test.go_to("google.com")

test.go_to("yahoo.com")

test.go_to("godaddy.com")

test.go_back()

test.go_forward()

test.autocomplete("go", 1)