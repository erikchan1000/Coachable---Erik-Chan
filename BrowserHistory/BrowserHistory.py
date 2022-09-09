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

    def deleteFront(self):
        if self.size == 0:
            return None

        elif self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            
    
    def delete(self, node):
        counter = 0

        if self.size == 0:
            return None
        curr  = self.head
        while counter < self.size:
            if curr == node:
                if self.size == 1:
                    self.head = None
                    self.tail = None

                else:
                    prev = curr.prev
                    prev.next = None
                    self.tail = prev

            counter += 1

    def addEnd(self, node):
        self.size += 1

        if self.head:
            node.next = self.head

        self.head = node
        
        if self.tail is None:
            self.tail = self.head
        return True



class BrowserHistory:
    def __init__(self):
        self.websites = DoublyLinkedList()
        self.currentPage = None
        self.hmap = {}
        self.currentIndex = 0

    def current_page(self):
        return self.currentPage

    # Traversal: Google -> Yahoo -> Facebook -> 

    # self.back = Google -> Yahoo -> Facebook -> Youtube

    def go_to(self, page):
        if self.currentPage and self.currentPage.next is not None:
            self.currentPage.next = None

        self.currentPage.next = Node(page)

        self.currentPage = self.currentPage.next

    def go_back(self):

        if self.currentPage and self.currentPage.prev:
            self.currentPage = self.currentPage.prev

        else:
            return None

    def go_forward(self):
        if self.currentPage and self.currentPage.next:
            self.currentPage = self.currentPage.next

        else:
            return None
            

    def skip_backward(self, N):
        count = 0 

        while count < N:
            count += 1
            self.go_back()

        return self.currentPage

    def skip_forward(self, N):
        count = 0

        while count < N:
            count += 1

            self.go_forward()

test = BrowserHistory()

test.go_to("test.com")