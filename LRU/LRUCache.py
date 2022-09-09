# get(k) -> value
#set(k, v)
#initialize cache w/ non-negative capacity (can be 0)

#"using" is just getting/setting that key

class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head = None, maxSize = 0):
        self.head = head
        self.tail = None
        self.size = 0
        self.maxSize = maxSize
        self.tail.next = self.head

        self.head.prev = self.tail

    def deleteEnd(self):
        if self.size == 0:
            return "Nothing to delete"

        elif self.size == 1:
            self.head = None
            self.tail = None

        else:
            prev = self.tail.prev
            prev.next = None
            self.tail = prev
            
    
    def delete(self, node):
        counter = 0

        if self.size == 0:
            return "Nothing to delete"
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

    def addFront(self, node):
        if self.size == self.maxSize:
            return ("Max Size Reached")

        else:
            self.size += 1

            if self.head:
                node.next = self.head

            self.head = node
            
            if self.tail is None:
                self.tail = self.head
            return True
    
class LRUCache:
    def __init__(self, size = 0):
        self.size = 0
        self.nodes = DoublyLinkedList(size = self.size)
        self.nodeMap = {}
        
    def get(self, key):
        if key in self.nodeMap:
            node = self.nodeMap.get(key)
            self.nodes.delete(node)
            self.nodes.addFront(node)

            return (node.key, node.value)

        else:
            return False


    def set(self, key, value):
        node = Node(key, value)
        self.map[key] = node
        self.nodes.delete(node)
        self.nodes.addFront(node)






    